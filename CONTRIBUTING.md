# Contributing

Keep Streamlit examples small, reproducible, and explicit about their validation status.

## Scope and safety

- Prefer synthetic or public data. Never commit private datasets, credentials, access tokens, or user/participant information.
- Bind local smoke runs to 127.0.0.1 unless a reviewed test specifically requires otherwise.
- Do not add persistent services, automatic deployment, or external write behavior without a separately reviewed change.
- Document runtime versions and any optional database, mapping, or geospatial dependencies.
- Label untested behavior as pending; do not describe a spot check as full runtime validation.

## Before opening a pull request

1. Review the example README, data paths, and dependency assumptions.
2. Run a syntax/import check using the target Python environment where possible.
3. Start the selected app in a disposable environment and exercise its main controls when feasible.
4. Check Markdown links and document the exact checks, versions, and limitations.
5. Confirm the change does not expose private data or introduce unreviewed network access.

A successful app startup is not a substitute for correctness, accessibility, security, or production testing. If the required environment is unavailable, say so explicitly.

## Security issues

Do not disclose exploitable vulnerabilities in a public issue. Contact zqmcomputing@gmail.com privately with a concise description and reproduction details that do not expose secrets or private data.

## License

Contributions are distributed under this repository's MIT license.
