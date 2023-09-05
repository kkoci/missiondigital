## This is the proof of concept for Nuvolar

### Tips on how to use it

  
This app has been `dockerized`, so all the process occurs inside docker containers.

- Clone this repo 

Once it has been cloned, run:

    docker build -t missiondigital1 .

This will build our base image, that we will run with *docker-compose*:

    docker-compose up

We can then send POST requests with, for example, Postman:

![Headers](https://i.imgur.com/VKa3Jui.png)
*We set up the headers*
![Wrong Body Payload](https://i.imgur.com/tf5Bvbc.png)
*We Set up the payload, this is an example of a wrong one*
![Correct Payload](https://i.imgur.com/rjhDce4.png)
Expected (correct) Payload 
![Expected Payload](https://i.imgur.com/rjhDce4.png)

Don't forget to run `docker-compose down` afterwards.

**

## Tests:

**

For the tests I have created another Docker Image, which has **Dockerfile.test** as name.

It can be built with:

    docker build -t missiondigitaltest -f .\Dockerfile.test .
And then ran with:

    docker run missiondigitaltest

![Visual example](https://i.imgur.com/07cFeVg.png)
 
There is a *workflow* for **Github Actions**, it has 2 jobs, one to **build/run/inspect** the container, and one to run the tests.

It is located at *.github/workflows/action.yml*

On push it will run the actions, You can clone this repo, then remove **THESE** characters and push to test it.
