# WA config file automatically generated by CK
device = "generic_android"
device_config = {
  "adb_name": "9886674d3359493432"
}
execution_order = "by_iteration"
instrumentation = [
  "execution_time",
  "interrupts",
  "cpufreq"
]
logging = {
  "colour_enabled": True,
  "file format": "%(asctime)s %(levelname)-8s %(name)s: %(message)s",
  "regular format": "%(levelname)-8s %(message)s",
  "verbose format": "%(asctime)s %(levelname)-8s %(name)s: %(message)s"
}
max_retries = 3
reboot_policy = "as_needed"
result_processors = [
  "status",
  "standard",
  "json"
]
retry_on_status = [
  "FAILED",
  "PARTIAL"
]
