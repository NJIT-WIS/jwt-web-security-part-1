# API Authentication and Authorization with JWT - Web Security Introduction - The Basics

Name:

UCID:

## Introduction

In this unit, you will be introduced to some basic concepts in web application security. You will learn about
authentication and authorization as well as learn about the supporting technology of HTTPS that secures the
communication between a web client and server. You will see how to store user passwords using hashing and understand the
different hashing algorithms. You will also learn the difference between encryption and hashing. In this project I am
providing you the complete user registration and login process as well as a demonstration of how to protect a route.

You must watch the video and read the reading in order to prepare yourself for project 2. I am not requiring you to do
anything with the code at this time; however, you should experiment with it and carefully review it, so that you can
implement it from scratch for your final project and properly test it. All you need to do is submit a link to the
repository back to campuse, so I know you accepted the assignment and hopefully went over all the material for the unit.

If you want to challenge yourself, you should implement this:

https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/  <-Adds logout essentially

and

https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/   <- Adds the ability to refresh expired tokens

You will need to implement this for your project, so I would get started on trying to do it now and test it!

* Note: This unit is focused only on this topic and does not include swagger, or JSONAPI, so that we can look at the
  fundamental concepts of security. We will be improving security and adding Swagger and JSONAPI spec back to the
  project over the next few lessons. Your final project will be to design and deploy a secure API that includes
  all the functionality that we have covered up until this point in the course.

### Unit Videos

[Watch this](https://youtu.be/B8UzrzECZzs)

### Required Readings

1. [Authentication vs Authorization](https://medium.com/plain-and-simple/identification-vs-authentication-vs-authorization-e1f03a0ca885)
2. [Understanding HTTPS](https://johnopdenakker.com/understanding-https/)
3. [Understanding SSL](https://blog.hubspot.com/marketing/what-is-ssl)
4. [Understanding RSA Encrpytion (basis of SSL)](https://comodosslstore.com/resources/what-is-an-rsa-algorithm-in-cryptography/)
5. [Understanding Hashing and Bcrypt](https://clerk.dev/blog/bcrypt-hashing-authentication-encryption)
6. [Types of Authentication used with Web Applications](https://medium.com/@vivekmadurai/different-ways-to-authenticate-a-web-application-e8f3875c254a)
7. [JWT vs. Sessions Authentication](https://ponyfoo.com/articles/json-web-tokens-vs-session-cookies)
8. [JWT Explained](https://arielweinberger.medium.com/json-web-token-jwt-the-only-explanation-youll-ever-need-cf53f0822f50)
9. [Big Summary of Authentication - Excellent Article](https://anil-pace.medium.com/json-web-tokens-vs-oauth-2-0-85dd0b32057d#2bd7)
10. [Refresh Tokens](https://www.loginradius.com/blog/identity/refresh-tokens-jwt-interaction/)

## Put a link to your Production Heroku Deployment Here

* [Production Deployment]()

## Instructions To Deploy To Heroku and Submit the Assignment

1. Clone this repo to your local
2. Submit a link to your assignment repository to Canvas

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest

### Future Notes and Resources
