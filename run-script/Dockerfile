# Use an official Ubuntu 18.04 as a parent image
FROM ubuntu:18.04

# Set the working directory to /app
WORKDIR /script

# Copy the current directory contents into the container at /script
ADD script.sh /script

# Update system, install additional packages, do anything you need
RUN apt update \
    && apt install -y figlet toilet \
    && chmod +x /script/script.sh
    
# Set the entrypoint
ENTRYPOINT ["/bin/bash"]

# Run the script when the container launches
CMD [ "script.sh"]


