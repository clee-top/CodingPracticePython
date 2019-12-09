Info: Notes and psuedocode pertaining to a tech screen

A: -> What I wrote at the time. Was presented over coderpad.
N: -> Notes after the fact. So I can remember what I wrote/answered at the time.

Use AWS Cli command line tool to process the following tasks -
1. Create a private key
A: aws create-key-pair <some_name>

2. Launch an EC2 instance
A: aws ec2 run-instances --image-id ami-xxxxxxxx (Probably an amazon image) --count 1 --instance-type t2.micro --key-name MyKeyPair(From above command) --security-group-ids sg-903004f8(Might have to make this, wizard makes one) --subnet-id subnet-6e7f829e (Only if you have a good subnet and VPC)
(Default VPC is open, don't use that.)

3. Login to the instance via ssh
A: ssh ec2-user@something.something (User varies by image)
N: Didn't need AWS cli for this, mild trick question?

4. Download a folder from some S3 bucket
A: aws s3 cp myfolder s3://mybucket/folder --recursive
N: I think I got the order wrong, shoulda been aws s3 cp s3://mybucket/folder/ myfolder/ --recursive

5. In said folder there is some python code (flask app), write a Dockerfile that will create an image that will that said flask app.
A:
```
FROM python-2/3.x(Version depends on pythonflavor)
ADD flask_source.xyz /working_dir.xyz
user some_flask_user
entrypoint['python', 'run_app']
```
N: Forgot to capitalize command "USER" and ENTRYPOINT. Made up what the entrypoint should be. Add assumes flask code is local to the Dockerfile when built.


6. Run the container and make sures it stays running.
A:
```
docker build -t some_flask_app:version .
docker push URL/.../.../some_flask_app:version (Or whatever repo you want.)
docker run -it some_flask_app:version
docker exec <some_pid> bin/bash
```



