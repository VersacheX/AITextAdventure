"""
Runtime service singletons used across TUI screens.

Mirrors the existing `client_api_requests.save_service_adapter` pattern
(module-level singleton + get/set functions) so screens can share state
(the configured save adapter, the logged-in user) without threading it
through every constructor.
"""