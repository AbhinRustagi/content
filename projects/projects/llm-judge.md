---
title: LLM Judge
date: 2026-01-30
description: An evaluation platform that uses LLMs to score question-answer pairs against custom, domain-specific criteria.
tags:
  - FastAPI
  - Next.js
  - LLM
  - Evaluation
  - Python
  - TypeScript
slug: llm-judge
thumbnail: projects/assets/llm-judge/thumbnail.png
published: true
canonical_url: https://www.abhin.dev/projects/llm-judge
github_url: https://github.com/AbhinRustagi/llm-judge
web_url: https://llm-judge-152003550665.australia-southeast1.run.app/
---

## Overview

LLM Judge is a web-based evaluation platform for scoring question-answer pairs using LLMs as judges. It targets regulated domains (legal, medical, finance) where QA quality matters and automated evaluation needs to be both rigorous and transparent.

Users upload a file of Q&A pairs, configure weighted evaluation criteria with optional hard minimums, pick a judge model, and get back per-pair scores with reasoning, a pass/fail verdict, and any safety warnings.

The goal was to build a flexible evaluation tool that supports multiple LLM providers, domain-aware criteria, and a transparent scoring breakdown — so users can understand _why_ something passed or failed, not just whether it did.

## Solution

A two-part system: a FastAPI backend that handles file parsing, safety checks, and LLM-based evaluation, and a Next.js frontend that guides users through a step-by-step wizard.

The evaluation engine runs all criteria concurrently for each Q&A pair using asyncio, with retry logic and exponential backoff per LLM call. Safety checks (jailbreak detection, bias detection) run independently using pattern matching and are reported separately from quality scores.

The verdict logic combines weighted criterion scores with hard minimums: an answer can fail even if its overall weighted score is above the threshold, if any single criterion falls below its hard minimum. This is important for domains like medical, where safety can't be traded off against other criteria.

## Tech Stack

- **Backend:** FastAPI, Pydantic, Uvicorn
- **Frontend:** Next.js 15 (App Router), React 19, TypeScript, Tailwind CSS, DaisyUI
- **LLM Providers:** OpenAI SDK, Anthropic SDK, Google GenAI SDK, DeepSeek (via OpenAI-compatible client)
- **File Processing:** PyMuPDF4LLM (PDF to Markdown), regex-based Q&A extraction
- **Resilience:** Tenacity (exponential backoff retries)
- **Deployment:** Docker, Google Cloud Run, Amazon Fargate

## Architecture

The frontend is a step-by-step wizard (domain → upload → criteria → model → evaluate → results) built with React 19 and DaisyUI components. It communicates with the FastAPI backend exclusively through a Next.js BFF proxy layer.

On the backend, the evaluation flow is:

1. Parse the uploaded file into Q&A pairs
2. Run safety checks (jailbreak + bias) concurrently on each pair
3. For each pair, evaluate all criteria concurrently — each criterion triggers an LLM call that returns a score (0-100), reasoning, and issues
4. Aggregate weighted scores, apply hard minimum logic, determine pass/fail verdict
5. Return the full evaluation response with per-pair results, summary statistics, and safety warnings

Provider abstraction maps model IDs to the correct SDK client, with a unified response format across all providers. Errors in individual evaluations are caught and reported as REJECT verdicts without failing the entire batch.
