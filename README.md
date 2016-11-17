# README: Turnitin Pittsburgh Back-end Coding Exercise

Welcome! We're excited you've decided to talk with us about a position on our
engineering team.

The purpose of this exercise is so we can have a conversation about your
technical background and abilities. We think that asking you to code on a
whiteboard during an interview isn't a great way to have a conversation. And
even if we sit down and pair during an interview it's a higher pressure
situation than it could be.

Instead we ask that you read these instructions and do an hour or two of work,
on your time, to complete the exercise. During the interview we'll talk about
decisions you've made, the resulting application, and how you might change it
given different circumstances.

Below are two sections:

* *Instructions*: the problem we'd like you to solve along with expectations we
  have about your solution.
* *Logistics*: constraints around the problem, and how we'd like you to
  communicate your solution to us

# Instructions

## Problem

We're starting a new application and we need to store students! We'd like to be
able to do the following with the students:

* Create a student
* Retrieve a particular student by unique identifier
* Search students in the system

__1.__ Format

The application should accept and produce JSON.

__2.__ Data

The student record has the following fields:

* An `id` that uniquely identifies the student. This will be provided by the
  server when the student is created and may not be changed.
* Either an `email` or a `username` must be non-blank, and whichever (or both)
  are defined the value must be unique within that field. Additionally, the
  `email` field should contain a superficially valid email.
* A `first_name` and `last_name`; the `last_name` is required to be non-blank.
* A `display_name`, which if not defined at creation should be the first name
  and last names joined with a space.
* The `created_at` datetime when the student was added to the system, which
  should be assigned by the system when the student is created. It should be
  formatted 'YYYY-MM-DD HH:mm:ss' -- for example '2016-11-08 22:18:03' for
  'November 8, 2016 at 10:18:03 PM'.
* The `started_at` date of the student started at an institution; if not
  specified it should be the date the student was added to the system. It
  should be formatted 'YYYY-MM-DD' -- for example, '2016-11-08' for 'November 8,
  2016'.

__3.__ Search

The students may be searched by the following fields:

* `name` (which is a partial match against any of the first name, last name,
  and display name)
* `username` (partial match)
* `email` (partial match)
* `started_after` (date formatted `YYYY-MM-DD` that will return students
  who started on or after a particular date)

If multiple fields provided any returned records must match all of them -- that
is, you should treat them as an `AND`. For example, the following query would
find students with 'Jen' in their name who started after 'November 15, 2016':

```
GET /students?name=Jen&started_after=2016-11-15
```

__4.__ Routes

The routes you should use are:

* Create a student: `POST /students`
* Search students: `GET /students`
* Retrieve a student: `GET /students/{id}` (where `{id}` is the value assigned
  by the server)
* Health check: `GET /` should return a successful HTTP status

__5.__ Other thoughts

During our discussion we'll talk about your code and decisions you've made.
We may also challenge assumptions in the problem, or add requirements. For
example:

* How might student data be changed?
* What if we wanted to create many students at once?
* What if we wanted to assign each student to a school? More than one school?
* What if we wanted to track whether the student has logged in?

## Languages and Environment

__1.__ Languages

You may use any of the following languages to solve this problem:

* Python
* JavaScript
* Ruby
* Go
* Java

__2.__ Dependencies

If you use external libraries you should use standard dependency management
tools to declare them -- for example, `requirements.txt` for Python projects,
`Gemfile` for Ruby projects, etc.

__3.__ Database

If you use a relational database please use Postgres.

__4.__ Docker (optional)

Using Docker (with a `Dockerfile`) is also just fine. We use Docker for
development, testing, and production here, but you're not required to know it
when you start.

__5.__ Testing

Unit tests are strongly encouraged.

__6.__ Guidance

Please include with your solution instructions on what we need to do to
run it.

## Checking your work

There is a directory in this repo `exercise/` with a script that you can use to
exercise your solution. You can run it in two ways:

__1.__ Run without Docker

The checker requires python to be installed and a particular module to be
installed.  [Virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
is a great way to manage and isolate dependencies, and you can do so with the
exercise like this, assuming you're using some sort of Unix-y command-line:

```
$ cd exercise
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

If you don't have `virtualenv` you can install with

```
$ sudo pip install virtualenv
```

Once you've got the environment setup you can run it like this:

```
$ python check.py http://myhost:8888
```

where `http://myhost:8888` is the URL where your solution is running.

It uses the same data every time to run its checks so you'll need to have a
clean datastore before you run it.

__2.__ Run with Docker

If you already have Docker installed you can build a container and
point it at your solution. Note that mapping the host on which your solution is
running (`myhost`, below) to the host known by the docker container may be
tricky.

```
$ cd exercise
$ docker build -t turnitin-check .
$ docker run --rm turnitin-check http://myhost:8888
```

# Logistics

__1.__ Timeframe

You should take a max of two hours to complete this exercise. We want to be
both respectful of your time and fair to other candidates who might not have
a whole weekend to work on it.

__2.__ Git

You will need to use git for this exercise. To get these instructions and a
repo with test scripts do the following:

1. [Create a bitbucket account](https://bitbucket.org/account/signup/) if you
don't already have one. For the examples below we assume a user `pusheen`.
2. Clone our repository:

```
# Using ssh
$ git clone git@bitbucket.org:lightsidelabs/backend-code-exercise.git

# Using https
$ git clone https://pusheen@bitbucket.org/lightsidelabs/backend-code-exercise.git
```

__3.__ Remote

Once you are done you can put your solution in your own repository by adding it
as a remote and pushing to it.

1. Create a new repo via the bitbucket UI, let's assume you call it
`backend-code-exercise` to mirror ours.
2. Please make the repository *private*, we'd like to make sure that every
candidate's work is his or her own.
3. Add your repo as a remote and push:

```
$ git remote add myrepo ssh://git@bitbucket.org:pusheen/backend-code-exercise.git
$ git push myrepo master
```

__4.__ Access

Give Bitbucket user `cwinters` read access to your repository.

__5.__ Notify us

At least a day before your in-person interview, email `cwinters@turnitin.com`
your repo address.
