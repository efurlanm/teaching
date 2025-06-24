```python
%%writefile mpi-example.f90
PROGRAM mpi_example
    USE mpi
    IMPLICIT NONE
    INTEGER :: rank, size, ierr, msg, status(MPI_STATUS_SIZE)
    CALL MPI_INIT(ierr)                              ! Inicializa o MPI
    CALL MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierr)   ! Obtém o número de processos
    CALL MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierr)   ! Obtém o identificador do processo
    IF (size /= 2) THEN
        PRINT *, "Este programa requer exatamente 2 processos."
    ELSE
        IF (rank == 0) THEN
            msg = 42  ! Mensagem a ser enviada
            CALL MPI_SEND(msg, 1, MPI_INTEGER, 1, 0, MPI_COMM_WORLD, ierr) 
            PRINT *, "Processo 0 enviou a mensagem:", msg
        ELSE IF (rank == 1) THEN
            CALL MPI_RECV(msg, 1, MPI_INTEGER, 0, 0, MPI_COMM_WORLD, status, ierr) 
            PRINT *, "Processo 1 recebeu a mensagem:", msg
        END IF
    END IF
    CALL MPI_FINALIZE(ierr)  ! Finaliza o MPI
END PROGRAM mpi_example
```

    Overwriting mpi-example.f90



```python
! mpif90 mpi-example.f90 -o mpi-example.out
```


```python
! mpirun -np 2 ./mpi-example.out
```

     Processo 0 enviou a mensagem:          42
     Processo 1 recebeu a mensagem:          42

