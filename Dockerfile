#use openjdk image
FROM openjdk:17

#set working directory
WORKDIR /app

#copy the java source code to container
COPY Main.java /app

#compile the java source code
RUN javac Main.java

#run the java application
CMD ["java","Main"]