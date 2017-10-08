# python3
'''
Input Format. The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.

Output Format. Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated
integers — the 0-based index of the thread which will process the 𝑖-th job and the time in
seconds when it will start processing that job.
'''
class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def LeftChild(i):
        return 2 * i

    def RightChild(i):
        return 2 * i + 1

    def SiftDown(self, i):
        min_index = i
        left = JobQueue.LeftChild(i)
        right = JobQueue.RightChild(i)

        if left <= len(self.next_free_time) - 1:
            if self.next_free_time[left][1] < self.next_free_time[min_index][1]:
                min_index = left
            elif self.next_free_time[left][1] == self.next_free_time[min_index][1] and self.next_free_time[left][0] < self.next_free_time[min_index][0]:
                min_index = left

        if right <= len(self.next_free_time) - 1:
            if self.next_free_time[right][1] < self.next_free_time[min_index][1]:
                min_index = right
            elif self.next_free_time[right][1] == self.next_free_time[min_index][1] and self.next_free_time[right][0] < self.next_free_time[min_index][0]:
                min_index = right

        if i != min_index:
            self.next_free_time[i], self.next_free_time[min_index] = self.next_free_time[min_index], self.next_free_time[i]
            self.SiftDown(min_index)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        # self.assigned_workers = [None] * len(self.jobs)
        # self.start_times = [None] * len(self.jobs)
        # next_free_time = [0] * self.num_workers
        # for i in range(len(self.jobs)):
        #   next_worker = 0
        #   for j in range(self.num_workers):
        #     if next_free_time[j] < next_free_time[next_worker]:
        #       next_worker = j
        #   self.assigned_workers[i] = next_worker
        #   self.start_times[i] = next_free_time[next_worker]
        #   next_free_time[next_worker] += self.jobs[i]

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.next_free_time = [None] + [[x, 0] for x in range(self.num_workers)]

        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self.next_free_time[1][0]
            self.start_times[i] = self.next_free_time[1][1]
            self.next_free_time[1][1] += self.jobs[i]
            self.SiftDown(1)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

