# Pypeline

A data pipelining application.

## Setup

Install python version >=3.14 and [uv](https://github.com/astral-sh/uv).

uv will manage the project install and all package management for you.

run `uv sync` to ensure your project is setup and ready.

run `uv run main.py` to start the application

## Core Runtime Dependencies

These runtime dependencies are required. Check [uv.lock](./uv.lock) for specific versions.

## Core Development Dependencies

These dependencies are required for active development work. Check [uv.lock](./uv.lock) for specific versions.

- [ty](https://github.com/astral-sh/ty) : type checker and language server

## Before Submitting Code

Ensure that your code does not cause any of the following to fail:

- ty check : `uv run ty check`
