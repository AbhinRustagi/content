---
title: Pixelink
date: 2025-01-01
description: A minimal, distraction-free markdown editor with rich text editing, document organization, and MCP server integration.
tags:
  - next.js
  - react
  - firebase
  - tiptap
  - typescript
slug: pixelink
thumbnail: projects/assets/pixelink/thumbnail.png
published: true
canonical_url: https://www.abhin.dev/projects/pixelink
web_url: https://pixelink.abhin.dev/
---

## Overview

Pixelink is a distraction-free markdown editor built as a web app. It provides rich text editing with a clean, minimal interface, letting users focus on writing without UI clutter. Documents are stored in Firebase with real-time autosave, and can be organized using folders and tags.

## Problem Statement

Most writing tools are either too simple (plain text editors) or too bloated (full word processors). I wanted something in between: a clean, focused editor with just enough organization and formatting features to be useful, without the overhead.

## Solution

A Next.js web app with a Tiptap-based rich text editor that supports markdown-style formatting, image uploads, tables, code blocks, and task lists. Documents are persisted in Firebase with autosave. A sidebar provides navigation across documents, folders, and tags. The app also exposes an MCP server, allowing AI assistants to read and manage documents programmatically via API keys.

## Tech Stack

- Next.js 15 (App Router, Turbopack)
- React 19
- TypeScript
- Tiptap (rich text editor)
- Firebase (Auth, Firestore, Storage)
- TanStack Query (data fetching)
- Zustand (client state)
- Tailwind CSS 4
- Radix UI (component primitives)
- MCP SDK (Model Context Protocol server)

## Key Features

- Rich text editing with markdown shortcuts, tables, code blocks, task lists, and image embeds
- Drag-and-drop and paste image upload
- Document organization via folders and tags
- Autosave with debounced persistence
- Export to Markdown and PDF
- Customizable font family and theme (light/dark)
- Keyboard shortcuts for common actions
- MCP server endpoint for AI assistant integration
- API key management for programmatic access
- Firebase authentication with session middleware
