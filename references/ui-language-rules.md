# UI Language Rules

Supported modes: Chinese UI, English UI, global Chinese/English switch.

For Chinese-facing apps, recommend Chinese UI.

If Chinese UI is selected, all visible UI text must be Chinese: titles, buttons, placeholders, loading states, error states, empty states, result labels, validation messages, copy/export prompts.

If global switch is selected, complexity +1 and strings should be centralized in `i18n/zh-CN.ts`, `i18n/en-US.ts`, or `lib/i18n.ts`.
