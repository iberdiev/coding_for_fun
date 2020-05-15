class TaskNode():
    """

    TaskNode is data sctructure for each task needed to implement critical path method.

    """
    def __init__(self, name, task):
        """
        Initializing each task to implement Critical Path Method.
        Takes 2 arguments:
            1) string - 'id/name of a task'
            2) list - [duration(int), [predecessors], 'description']
        >>> task_A = TaskNode('A', [6, [], 'Earn money']) 
        >>> print(task_A.name)
        A
        >>> print(task_A.duration)
        6
        >>> print(task_A.description)
        Earn money
        """
        self.name = name
        self.duration = task[0]
        self.description = task[2]
        self.early_start = None
        self.early_finish = None
        self.late_start = None
        self.late_finish = None
        self.slack = None
        self.predecessors = []
        self.successors = []

class Project():
    """
    
    Implementation of a project entity in Critical Path Method.

    """
    def __init__(self, tasks):
        """
        Initializing project instances that takes dictionary of tasks as an input.
        Initialization includes execution of methods:
            1) build_network;
            2) find_early_points;
            3) find_late_points
            4) find_project_duration;
            5) find_node_slacks;
            
        Each task is represented as key, value pairs such as:
            key = 'id/name of a task' (string)
            value = [duration(int), [predecessors], 'description']
        >>> tasks = {                                    \
                        'A': [2, [], 'Learn python'],    \
                        'B': [4, ['A'], 'Do programming']\
                    }
        >>> project_A = Project(tasks)
        >>> type(project_A)
        <class '__main__.Project'>

        Attributes:
            duration - duration of the project.
            n_of_tasks - number of tasks for the project.
            first_jobs - jobs at the start, saved as a dictionary.
            last_jobs - jobs at the end, saved as a dicationary.
            tasks - all the jobs, saved as a dictionary.
        """
        self.duration = None
        self.n_of_tasks = None
        self.first_jobs = {}
        self.last_jobs = {}
        self.tasks = {}
        self.build_network(tasks)
        self.find_early_points()
        self.find_late_points()
        self.find_project_duration()
        self.find_node_slacks()

    def build_network(self, tasks):
        """
        Method that is used in __init__ to build project's structure.
        
        1) finds projects object's attributes:
            - n_of_tasks;
            - first_jobs;
            - last_jobs;
            - tasks;
        2) gives a structures by decraling predecessors and successors for each task.
        """
        self.n_of_tasks = len(tasks)
        to_remove, processed_tasks = [],[]
        for task in tasks:
            if not tasks[task][1]:
                to_remove.append(task)
                self.first_jobs[task] = TaskNode(task, tasks[task])
        self.tasks = self.first_jobs.copy()
        for task in to_remove:
            processed_tasks.append(task)
            del tasks[task]
        while tasks:
            temp, to_remove = [], []
            for task in tasks:
                for predecessor in tasks[task][1]:
                    if predecessor in processed_tasks:
                        if task not in self.tasks:
                            if task not in self.tasks: processed_tasks.append(task)
                            to_remove.append(task)
                            new_task = TaskNode(task, tasks[task])
                            new_task.predecessors.append(self.tasks[predecessor])
                            self.tasks[task] = new_task
                            self.tasks[predecessor].successors.append(new_task)
                        else:
                            self.tasks[task].predecessors.append(self.tasks[predecessor])
                            self.tasks[predecessor].successors.append(self.tasks[task])            
            for task in to_remove: del tasks[task]
        for task in self.tasks:
            if not self.tasks[task].successors: self.last_jobs[task] = self.tasks[task]
    def find_early_points(self):
        """
        Method that is used in __init__ to find early start and end times for each task.
        """
        tasks_left = []
        for task in self.first_jobs:
            self.first_jobs[task].early_start = 0
            self.first_jobs[task].early_finish = self.first_jobs[task].duration
            if self.first_jobs[task].successors:
                for successor in self.first_jobs[task].successors:
                    if successor not in tasks_left: tasks_left.append(successor)
        late_start_times = {}
        for task in tasks_left:
            late_start_times[task.name] = [pred.early_finish for pred in task.predecessors if pred.early_finish]
        while tasks_left:
            to_remove = []
            for task in tasks_left:
                if len(task.predecessors) == len(late_start_times[task.name]):
                    self.tasks[task.name].early_start = max(late_start_times[task.name])
                    self.tasks[task.name].early_finish = max(late_start_times[task.name]) + task.duration
                    to_remove.append(task.name)
                    for successor in task.successors:
                        if successor.name not in late_start_times: late_start_times[successor.name] = []
                        late_start_times[successor.name].append(max(late_start_times[task.name]) + task.duration)
                        if successor not in tasks_left: tasks_left.append(successor)
            i = 0
            while i < len(tasks_left):             
                if tasks_left[i].name in to_remove:
                    to_remove.remove(tasks_left.pop(i).name)
                else: i+= 1
    def find_late_points(self):
        """
        Method that is used in __init__ to find late start and end times for each task.
        """
        tasks_left = []
        max_early_finish = max([self.tasks[task].early_finish for task in self.last_jobs])
        for task in self.last_jobs:
            self.last_jobs[task].late_start = max_early_finish - self.last_jobs[task].duration
            self.last_jobs[task].late_finish = max_early_finish
            if self.last_jobs[task].predecessors:
                for predecessor in self.last_jobs[task].predecessors:
                    if predecessor not in tasks_left: tasks_left.append(predecessor)
        late_start_times = {}
        for task in tasks_left:
            late_start_times[task.name] = [pred.late_start for pred in task.successors if pred.late_start]
        while tasks_left:
            to_remove, to_add = [], set()
            for task in tasks_left:
                if len(task.successors) == len(late_start_times[task.name]):
                    self.tasks[task.name].late_finish = min(late_start_times[task.name])
                    self.tasks[task.name].late_start = min(late_start_times[task.name]) - task.duration
                    to_remove.append(task.name)
                    for predecessor in task.predecessors:
                        if predecessor.name not in late_start_times: late_start_times[predecessor.name] = []
                        late_start_times[predecessor.name].append(min(late_start_times[task.name]) - task.duration)
                        if predecessor not in tasks_left:
                            if predecessor not in tasks_left: tasks_left.append(predecessor)
            i = 0
            while i < len(tasks_left):
                task_name = tasks_left[i].name
                if task_name in to_remove:
                    tasks_left.pop(i)
                    to_remove.remove(task_name)

                else: i+= 1
            
    def find_project_duration(self):
        """
        Method that is used in __init__ to find duration of the project.
        """
        self.duration = max([self.tasks[task].early_finish for task in self.last_jobs])
    def find_node_slacks(self):
        """
        Method that is used in __init__ to find slack for each task.
        """
        for task in self.tasks:
            self.tasks[task].slack = self.tasks[task].late_start - self.tasks[task].early_start
    def get_critical_path(self):
        """
        Method that returns a string that illustrates criticial path for the project.
        >>> tasks = {                          \
                        'A': [4, [], ''],      \
                        'B': [6, [], ''],      \
                        'C': [4, ['B'],''],    \
                        'D': [12, ['A'],''],   \
                        'E': [7, ['A','C'],''],\
                        'F': [9, ['B'],''],    \
                        'G': [5, ['E','F'],''],\
                    }
        >>> my_project = Project(tasks)
        >>> critical_path = my_project.get_critical_path()
        >>> print(critical_path)
        B -> C -> E -> G
        """
        for task in self.first_jobs:
            if not self.first_jobs[task].slack:
                critical_path = [task]
                break  
        while critical_path[-1] not in self.last_jobs:
            for task in self.tasks[critical_path[-1]].successors:
                if not task.slack:
                    critical_path.append(task.name)
                    break
        return ' -> '.join(critical_path)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    tasks = {
        'A': [10, [], ''],
        'B': [12, ['A','D'], ''],
        'C': [9, ['B'],''],
        'D': [5, [],''],
        'E': [7, ['D','G'],''],
        'F': [6, ['E'],''],
        'G': [3, [],''],
        'H': [4, ['G'],''],
        'I': [6, ['H'],'']
        }

    project = Project(tasks)
    print(f'After change:\nDuration: {project.duration}\nCritical Path: {project.get_critical_path()}')

'''
    Critical Path Method

    Duration of the project is time period requires to complete the project. It is easy to calculate
duration for a sequence of activities by adding duration of each activity. However, for projects we
can have mixed types of activities, such that some of them may not depend on each other.
Consequently, we can do several activities at the same time.

    Critical Path Method is a way to calculate and analyze timings for any kinds of projects, knowing
only structure/dependencies of the tasks, and their duration. For example, we have 2 independent
tasks to complete with duration A = 1, B = 2. We can intuitively claim that if they are independent,
we need 2 units of time to complete the job. And the critical path is B, meaning that if me
completed task B, task A will be automatically will be completed, because they are independent and
the duration is smaller.

    Critical path, it is a path such that it has maximum units of time compared to all other paths possible
to generate. Meaning that, critical path with its minimum possible duration that needs to complete
the project. We cannot shift timings for critical path, because it will increase the duration of whole
project. Moreover, we can tell for how long we can shift tasks that are not on critical path by
calculating their slack. However, we can shift for some units of time for others tasks, that are not in
critical path.

    In our previous primitive example, critical path is only B, meaning that if we delay task B, our
whole project's duration will increase. On the other hand, if we delay project A for 1 unit of time,
we can still finish it on the next unit, because task B needs 2 units of duration.
Application of Critical Path methods is extremely helpful in any problem that has
scheduling, and can be optimized. One of the examples can be in real project management. If we
have different tasks, but currently do not have enough employers, we can delay tasks not on the
critical path, until we hire enough people. We faced the problem of lacking enough human
resources, however were able to use Critical Path Method, and we finished the project in planned
time.

Answers for the test assignment generated by code:
    1) duration = 22
    2) critical_path = 'B -> C -> E -> G'
    3) absolutely no effect, because F is not on critical path, and when F's duration was 9, slack was 2,
        can delay task F for 2 weeks.Data Structure

I tried to think in object-oriented way and decided to choose 2 entities: Project and Task.

Task:
    - name (string)
    - duration (integer)
    - description (string)
    - early start (integer)
    - early finish (integer)
    - late start (integer)
    - late finish (integer)
    - slack (integer)
    - predecessors (list of Task node instances)
    - successors(list of Task node instances)
Project:
    - duration (integer)
    - number of tasks (integer)
    - first jobs (Python dictionary: key:value pairs where key is a name of task, and value is Task
    instance described previously)
    - last jobs (Python dictionary: key:value pairs where key is a name of task, and value is Task
    instance described previously)
    - tasks (Python dictionary: key:value pairs where key is a name of task, and value is Task
    instance described previously)
    This structure works well when implementing Critical Path Method for several reasons:
    - project object has first and last jobs so we know from where to begin, and where to finish;
    - tasks that has all the tasks including those mentioned above, so we can refer to any of the
    task in the project without searching them from the start or end;
    - each task has predecessors and successors lists, so we can structure the project and keep
    the dependencies of tasks;
'''