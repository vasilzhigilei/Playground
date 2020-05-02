package main

import (
	"fmt"
	"log"

	"github.com/emersion/go-imap"
	"github.com/emersion/go-imap/client"
)

func main() {
	log.Println("Connecting to server...")

	// Connect to server
	c, err := client.DialTLS("imap.gmail.com:993", nil)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Connected")

	// Don't forget to logout
	defer c.Logout()

	var password, username string
	log.Println("Enter email username: ")
	fmt.Scanf("%s", &username)
	log.Println("Enter password: ")
	fmt.Scanf("%s", &password)
	// Login
	if err := c.Login(username, password); err != nil {
		log.Fatal(err)
	}
	log.Println("Logged in")

	// List mailboxes
	mailboxes := make(chan *imap.MailboxInfo, 10)
	done := make(chan error, 1)
	go func () {
		done <- c.List("", "*", mailboxes)
	}()

	log.Println("Mailboxes:")
	for m := range mailboxes {
		log.Println("* " + m.Name)
	}

	if err := <-done; err != nil {
		log.Fatal(err)
	}

	// Select INBOX
	mbox, err := c.Select("eBay", false)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Flags for INBOX:", mbox.Flags)

	// get all messages
	from := uint32(1)
	to := mbox.Messages

	seqset := new(imap.SeqSet)
	seqset.AddRange(from, to)

	messages := make(chan *imap.Message, 10)
	done = make(chan error, 1)

	var section imap.BodySectionName
	items := []imap.FetchItem{section.FetchItem()}

	go func() {
		done <- c.Fetch(seqset, items, messages)
	}()

	log.Println("All messages:")
	for msg := range messages {
		log.Println("* " + msg.Envelope.Subject)
		log.Println(msg.GetBody(&section))
	}

	if err := <-done; err != nil {
		log.Fatal(err)
	}

	log.Println("Done!")
}