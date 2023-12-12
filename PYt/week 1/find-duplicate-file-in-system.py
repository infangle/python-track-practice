class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        answer = []
        path_dict = defaultdict(list)

        for path in paths:
            directory = list(path.split())
            for i in range(1, len(directory)):
                string = list(directory[i].split('('))
                path_dict[string[1]].append(directory[0] + "/" + string[0])

        for key, value in path_dict.items():
            if len(value) > 1:
                answer.append(value)

        return answer