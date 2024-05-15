def job_sequencing(jobs):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline to determine the size of the timeline
    max_deadline = max(job[1] for job in jobs)
    
    # Initialize the timeline with None (to represent empty slots)
    timeline = [None] * max_deadline
    
    total_profit = 0
    
    # Place each job in the latest possible slot before its deadline
    for job in jobs:
        job_id, deadline, profit = job
        for slot in range(deadline - 1, -1, -1):
            if timeline[slot] is None:
                timeline[slot] = job_id
                total_profit += profit
                break
    
    # Remove None values to get the scheduled jobs
    scheduled_jobs = [job_id for job_id in timeline if job_id is not None]
    
    return scheduled_jobs, total_profit

# Example usage
if __name__ == "__main__":
    # Jobs are represented as tuples: (job_id, deadline, profit)
    jobs = [
        ('a', 2, 100),
        ('b', 1, 19),
        ('c', 2, 27),
        ('d', 1, 25),
        ('e', 3, 15)
    ]
    
    scheduled_jobs, total_profit = job_sequencing(jobs)
    print(f"Scheduled jobs: {scheduled_jobs}")
    print(f"Total Profit: {total_profit}")