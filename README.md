# microlearning-api
A Python FastAPI that powers a microlearning application

# Instructions to setup locally

## Make sure to have [uv](https://docs.astral.sh/uv/) installed

### MacOS (Homebrew)
```
brew install uv
```

### Windows (Powershell)
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Install Python 3.12 and activate the virtual env


### MacOS
```
uv python install 3.12 && source .venv/bin/activate
```
### Windows (Powershell)
```
uv python install 3.12; .venv\Scripts\Activate.ps1
```

## Install Dependencies

```
uv install
```

## Run FastAPI Server

```
uv run uvicorn main:app --reload
```








