from collections import deque
# Station 객체 초기화
class Station:
    # 객체 초기화 메서드
    def __init__(self, name):
        # 지하철 명 변수 초기화
        self.name = name
        # 이웃한 역을 담는 list 변수 초기화
        self.neighbors = []

    # 이웃역 추가 메서드
    def add_connection(self, another_station):
        self.neighbors.append(another_station.name)
        another_station.neighbors.append(self.name)
# 역 간 최단거리 탐색 메서드
def bfs(start, goal):

    # 변수정의
    previous = {}
    station_queue = deque()
    current = None

    # 초기설정
    previous[start] = None
    station_queue.append(start)

    while len(station_queue) > 0 and start != goal:
        # 큐의 가장 첫번째 역을 가져온다
        current = station_queue.popleft()
        # 그 역의 이웃역 리스트를 불러온다
        current_neighbors = stations[current.name].neighbors
        # 이웃한 역들에 대해 조사
        for i in current_neighbors:
            # 이미 확인한 역이 아니라면
             if stations[i] not in previous:
                 # 큐에 추가
                station_queue.append(stations[i])
                 # 이전기록에 추가
                previous[stations[i]] = current

        if current == goal:
            result = goal
            path = [goal]
            while result != start:
                result = previous[result]
                path.append(result)
            return path
    return None

stations = {}
in_file = open('stations.txt', 'rt', encoding='UTF-8-sig')

for line in in_file:
    list = line.strip().split(' - ')

    for i in range(len(list)):
        station = Station(list[i].strip())
        if i == 0:
            station.add_connection(Station(list[i + 1].strip()))
        elif i == len(list) - 1:
            station.add_connection(Station(list[i - 1].strip()))
        else:
            station.add_connection(Station(list[i + 1].strip()))
            station.add_connection(Station(list[i - 1].strip()))
        # 이미 존재하는 station에 이웃하는 역 추가
        if(station.name in stations):
            station.neighbors = stations[station.name].neighbors + (station.neighbors)
        stations[station.name] = station

in_file.close()

# 테스트
start_name = "이태원"
goal_name = "노량진"
start = stations[start_name]
goal = stations[goal_name]
path = bfs(start, goal)
for station in path:
    print(station.name)