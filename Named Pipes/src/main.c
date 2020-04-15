#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
  // Open fd for named pipe
  int pipe = open("pipe", O_RDWR);

  // Create placeholder for message
  const char * msg = "ok woooow this is epic oh yeah alright\n";

  for(int x = 0; x < 10; x++)
  {
    printf("[i] Writing data to pipe...\n");

    // Write data to pipe
    if((size_t) write(pipe, msg, strlen(msg)+1) < strlen(msg)) // write() failed
    {
      printf("[!] Failed to write message to named pipe\n");
      return 1;
    }

    printf("[i] Waiting 1 second before retrying...\n");

    sleep(1);
  }

  // Close fd
  close(pipe);

  return 0;
}
