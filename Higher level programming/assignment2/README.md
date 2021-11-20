# README.md Assignment2 Rosa Alsgaard rnalsgaa

updated: 14/09/21 09:28

## Task 2.1

### Prerequisites

following code ...

   $  ./move.sh src_dir dst_dir file_ending
or
   $  ./move.sh src_dir dst_dir

... should work on ifi machines


### Functionality

- move.sh can create dst_dir if it does not exist and the user wishes so
- move.sh tells user what command line arguments to use if usage is wrong
- User can enter relative path to src_dir and dst_dir
- User can choose to move all files and directories or specified file types


### Missing Functionality

Errors not handled by move.sh script
- User tries to move specified file types (ex py, java, txt) and they're not found in src_dir
- User tries to move files from src_dir to src_dir
- No error displayed when moving files from empty directory
- User may not choose name of new directory in case of non existing destination
  directory

### Usage

Move all files from src_dir to dst_dir use:

   $   ./move.sh src_dir dst_dir

Move only .filetype-files from src_dir to dst_dir use:

   $   ./move.sh src_dir dst_dir filetype

## Task 2.2

### Prerequisites

- ~/.local/share/timer_logfile.txt might be created manually first time
script runs, but error still occurs regarding this.

- First time script runs theres a bug when I try to read first line in the empty
timer_logfile.txt. This is not fatal. (line 12 in track)

- I forgot to comment the code.

### Functionality

- This script can track simple labeled tasks, and log them.
- Tracks tasks exceeding 24h.
- The scripts throws cool unwanted errors.


### Missing Functionality

- Labels must be without empty space, if not the whole label will not be
  registered.
- Unwanted errors first time a task is tracked. This is not fixed due to lack of time.

### Usage

Starts tracking task without label (not recommended)
   $   ./track start

Starts tracking task with label
   $   ./track start my_label

Stops tracking current task if theres an active task
   $   ./track stop

Shows current task if theres an active task
   $   ./track status

Displays running time of all ended tasks
   $   ./track log
