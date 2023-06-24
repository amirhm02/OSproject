#include <iostream>
#include <sys/ipc.h>
#include <sys/shm.h>

using namespace std;

#define BUFFER_SIZE 10

struct shared_buffer {
    int buffer[BUFFER_SIZE];
    int in;
    int out;
};

int main() {
    key_t key = ftok("shared_memory", 'R');
    int shmid = shmget(key, sizeof(shared_buffer), 0666|IPC_CREAT);
    if (shmid == -1) {
        cerr << "Error creating shared memory segment" << endl;
        return 1;
    }

    shared_buffer *buffer = (shared_buffer*) shmat(shmid, NULL, 0);
    if (buffer == (void*) -1) {
        cerr << "Error attaching to shared memory segment" << endl;
        return 1;
    }

    
    buffer->in = 0;
    buffer->out = 0;

    
    for (int i = 0; i < BUFFER_SIZE; i++) {
        while (((buffer->in + 1) % BUFFER_SIZE) == buffer->out); 
        buffer->buffer[buffer->in] = i; 
        cout << "Produced item: " << i << endl;
        buffer->in = (buffer->in + 1) % BUFFER_SIZE; 
    }

    
    for (int i = 0; i < BUFFER_SIZE; i++) {
        while (buffer->in == buffer->out); 
        int item = buffer->buffer[buffer->out]; 
        cout << "Consumed item: " << item << endl;
        buffer->out = (buffer->out + 1) % BUFFER_SIZE; 
    }

    
    if (shmdt(buffer) == -1) {
        cerr << "Error detaching from shared memory segment" << endl;
        return 1;
    }

    
    if (shmctl(shmid, IPC_RMID, NULL) == -1) {
        cerr << "Error deleting shared memory segment" << endl;
        return 1;
    }

    return 0;
}
