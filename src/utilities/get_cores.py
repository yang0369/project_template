def get_cpu_limit() -> int:
    """
    Detects the number of CPU cores available to the OCP pod
    
    Returns:
        The integer number of CPU cores available
    """
    try:
        with open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us") as f:
            quota = int(f.read())
        with open("/sys/fs/cgroup/cpu/cpu.cfs_period_us") as f:
            period = int(f.read())

        # If quota is -1, it means there is no limit
        # In this case, we fall back to the host's CPU count
        if quota == -1:
            return os.cpu_count()

        return math.ceil(quota / period)

    except (FileNotFoundError, ValueError):
        # For running on Windows/macOS
        return os.cpu_count()
