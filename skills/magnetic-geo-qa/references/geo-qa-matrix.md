# Geographic QA matrix

Use the same fields for every observation:

- `requested_location`, `observed_location`, `exit_evidence`
- `timestamp_utc`, `browser`, `device`, `viewport`, `locale`
- `initial_url`, `redirect_chain`, `final_url`, `status`
- `language`, `currency`, `displayed_offer`, `availability`
- `consent_experience`, `creative_or_placement`, configured visible text
- `screenshot`, failed resources, `validation_status`, notes, confidence

Keep browser contexts, cookies, storage, and sticky sessions isolated per country. A successful status is acceptable only when expected content is present. Preserve missing screenshots and fields as missing rather than fabricating a result.
