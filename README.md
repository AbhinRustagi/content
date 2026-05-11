# content

Source content for [abhin.dev](https://www.abhin.dev). A monorepo that
aggregates what used to live in separate repositories so it can be
versioned, indexed, and deployed together.

## Structure

- [blog/](blog/) — blog posts (Markdown + frontmatter). Auto-published to
  [Medium](https://www.medium.com/@abhinr) on push to `main`. See
  [blog/README.md](blog/README.md) for the post index.
- [projects/](projects/) — project writeups and case studies. See
  [projects/README.md](projects/README.md) for the project index.
- [books/](books/) — reserved for future book notes; currently empty.

Each content area keeps its own indexed `README.md` (updated automatically
by [repo-db-indexer](https://github.com/abhinrustagi/repo-db-indexer)) and
its own `index.json` projection consumed by the website.

## Workflows

- **Index and Publish Blog** ([`.github/workflows/index-and-publish-blog.yml`](.github/workflows/index-and-publish-blog.yml))
  — runs on changes under `blog/`. Publishes any new posts to Medium and
  refreshes [blog/README.md](blog/README.md) + [blog/index.json](blog/index.json).
- **Index Projects** ([`.github/workflows/index-projects.yml`](.github/workflows/index-projects.yml))
  — runs on changes under `projects/`. Refreshes [projects/README.md](projects/README.md)
  + [projects/index.json](projects/index.json) and commits the result.

Both workflows scope to their content subdirectory via the indexer's
`working-directory` input, so links inside the per-area READMEs remain
relative to that area.
