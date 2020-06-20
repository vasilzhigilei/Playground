## Some notes taken during an MPI seminar

MPI
* distributed memory

OpenMP
* shared memory

## Granularity
Coarse grained: lots of computation, little (or no) communication
Fine grained: more evenly distributed between computation and communication
Granularity determines whether special hardware is required

## MPI
Usually when MPI is run, the number of processes is determined and fixed for the lifetime of the program
MPI programs run under the control of an executor
Each copy has its own global variables, stack, heap, and program counter

Must initialize MPI prior to using (Python mpi4py calls this when a communicator object is instantiated)
Determine communicator size (number of processes)
Determine process rank
Finally, finalize MPI (shut down MPI), freeing up MPI resources after all other MPI library calls
