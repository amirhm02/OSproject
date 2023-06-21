#include <iostream>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>

using namespace std;

struct Buffer {
    int data;
    bool full;
};

int main() {
    const int SIZE = sizeof(Buffer);
    const char* NAME = "buffer";


    int shm_fd = shm_open(NAME, O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, SIZE);

    
    void* ptr = mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);

    
    Buffer* buffer = static_cast<Buffer*>(ptr);
    buffer->full = false;

    
    pid_t pid = fork();

    if (pid == 0) {
        
        while (true) {
            if (buffer->full) {
                cout << "Consumer: " << buffer->data << endl;
                buffer->full = false;
            }
        }
        exit(0);
    } else if (pid > 0) {
        
        int i = 0;
        while (true) {
            if (!buffer->full) {
                buffer->data = i++;
                buffer->full = true;
            }
            usleep(100000); 
        }
        exit(0);
    } else {
        cerr << "Fork failed" << endl;
        exit(1);
    }

    return 0;
}