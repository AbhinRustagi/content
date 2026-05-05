---
title: "@react-volatile"
date: 2026-01-01
description: Chaos engineering for React; inject controlled failures into hooks, components, and async logic.
tags:
  - React
  - TypeScript
  - Chaos Engineering
  - Babel
slug: react-volatile
thumbnail: projects/assets/react-volatile/thumbnail.png
published: true
canonical_url: https://www.abhin.dev/projects/react-volatile
github_url: https://github.com/AbhinRustagi/react-volatile
web_url: https://abhinrustagi.github.io/react-volatile
---

## Overview

react-volatile is a chaos engineering toolkit for React. It wraps standard React hooks (`useState`, `useEffect`, `useReducer`, `useMemo`, `useCallback`) with chaos-injecting counterparts that randomly introduce delays, errors, data corruption, and timeouts during development and testing. The idea is to surface resilience gaps early — before they show up in production.

The library is split into three packages: a framework-agnostic chaos engine (`@react-volatile/core`), React bindings (`@react-volatile/react`), and a Babel plugin (`@react-volatile/babel-plugin`) that can automatically transform standard hooks into their volatile versions.

## Motivation

React apps tend to be built and tested under ideal conditions — fast networks, no errors, predictable state transitions. But production is different: API calls time out, state updates arrive late, effects fail silently. Most of these failure modes only surface after deployment.

Chaos engineering addresses this by injecting faults intentionally, but existing tools target backend infrastructure (network partitions, container failures). There wasn't a good option for testing React component resilience at the hook level. react-volatile fills that gap.

## How It Works

The core of the library is the `ChaosEngine`, which decides whether to inject a fault on any given hook invocation. The decision depends on:

1. **Probability** — a configurable likelihood (default 30%) checked against a seeded PRNG (Mulberry32), so chaos sequences are reproducible across runs.
2. **Chaos type** — each hook category (state, effect, async, render, etc.) can be enabled or disabled independently.
3. **Targeting** — faults can be scoped to specific components using name patterns or regex, with include/exclude lists.
4. **Scheduling** — three modes: continuous (always active), burst (alternating on/off intervals), or scheduled (specific time windows).

When a fault triggers, the engine selects a failure mode from the allowed set for that chaos type:

- **State/Reducer:** delay the update, throw an error, or corrupt the value
- **Effect:** delay execution, throw, or skip entirely
- **Async:** delay resolution, reject the promise, or simulate a timeout
- **Render:** throw during render, delay mounting, or return empty output

Every injected fault is logged as a `ChaosEvent` with metadata (type, failure mode, target, timestamp), which feeds into the built-in DevTools panel.

## Architecture

The monorepo contains three packages:

**@react-volatile/core** — The chaos engine, seeded randomizer, event logger, scheduler, and type definitions. No React dependency. This could be adapted to other frameworks.

**@react-volatile/react** — React bindings built on top of core:

- `VolatileProvider` wraps the app and manages the engine lifecycle
- `useVolatileState`, `useVolatileEffect`, `useVolatileReducer`, `useVolatileMemo`, `useVolatileCallback` — drop-in replacements for their React counterparts, with optional per-hook configuration
- `useVolatileAsync` — an async wrapper that returns `{data, error, loading, execute}` with chaos applied to the async operation
- `withVolatile` — a HOC for component-level render chaos
- `ChaosPanel` — a DevTools overlay (toggled with `Ctrl+Shift+V`) showing a live event log
- `ChaosIndicator` — a small floating badge showing the event count

**@react-volatile/babel-plugin** — Transforms standard React hook calls (`useState` → `useVolatileState`, etc.) at build time. Supports two modes: transform all hooks, or only hooks annotated with a `@volatile` comment. Injects metadata (component name, hook name, source location) so the DevTools panel can trace faults back to their origin.

## Tech Stack

- TypeScript
- React 19
- Babel (plugin development)
- Vitest (testing)
- pnpm (monorepo management)

## Key Decisions

**Seeded PRNG over Math.random.** Using a Mulberry32 generator with an optional seed means chaos sequences are deterministic. If a test fails due to an injected fault, setting the same seed reproduces the exact same sequence of failures. This makes debugging feasible — without it, chaos testing would be frustrating rather than useful.

**Separate core from React.** Keeping the engine framework-agnostic means the chaos logic (probability, scheduling, targeting, event tracking) is testable without React, and could be reused for Vue or Svelte bindings. The React package is a thin layer of hooks and context on top.

**Babel plugin for zero-effort adoption.** Manually replacing every `useState` with `useVolatileState` across a codebase is tedious and invasive. The Babel plugin makes adoption a single config change, with the `@volatile` annotation mode available for teams that want more control over which hooks are affected.
