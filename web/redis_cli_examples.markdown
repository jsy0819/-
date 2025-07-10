# Redis CLI 예제

이 문서는 Redis CLI를 사용해 Redis 서버와 상호작용하는 예제를 제공합니다. 초보자를 위해 기본 데이터 구조와 작업을 다루며, 실무 시나리오를 포함해 학습을 지원합니다.

## 기본 연결

Redis CLI에 연결하려면 다음 명령어를 입력하세요:

```bash
redis-cli
```

- **출력**: `127.0.0.1:6379>`
- **설명**: 기본 호스트(127.0.0.1)와 포트(6379)에 연결.

Docker를 사용하는 경우:

```bash
docker exec -it my-redis redis-cli
```

- **설명**: Docker 컨테이너 `my-redis`의 Redis CLI에 접속.

Windows 10에서 WSL2를 사용하는 경우, WSL2 IP로 연결:

```bash
redis-cli -h <WSL2_IP>
```

- **설명**: `wsl hostname -I`로 IP 확인.

## 문자열 예제

문자열은 텍스트, 숫자, 바이너리 데이터를 저장하는 기본 데이터 타입입니다.

### 키-값 쌍 설정

```redis
SET name "Alice"
```

- **출력**: `OK`
- **설명**: "name" 키에 "Alice" 값을 설정. 성공 시 `OK` 반환.

### 값 조회

```redis
GET name
```

- **출력**: `"Alice"`
- **설명**: "name" 키의 값을 조회.

### 만료 시간 설정

```redis
SETEX session 3600 "session_data"
```

- **출력**: `OK`
- **설명**: "session" 키에 "session_data" 값을 설정, 3600초(1시간) 후 만료.

### 남은 만료 시간 확인

```redis
TTL session
```

- **출력**: `(integer) 3600`
- **설명**: "session" 키의 남은 만료 시간(초) 반환.

### 카운터 증가

```redis
INCR counter
```

- **출력**: `(integer) 1`
- **설명**: "counter" 키의 값을 1 증가, 처음이면 1로 설정.

### 카운터 감소

```redis
DECR counter
```

- **출력**: `(integer) 0`
- **설명**: "counter" 키의 값을 1 감소.

**실무 예**: 블로그 게시물 조회수 추적 (`INCR post:1:views`).

## 리스트 예제

리스트는 순서가 있는 문자열 컬렉션으로, 큐나 스택으로 사용됩니다.

### 리스트 머리에 추가

```redis
LPUSH tasks "Task 1"
```

- **출력**: `(integer) 1`
- **설명**: "tasks" 리스트의 머리에 "Task 1" 추가, 리스트 길이 반환.

### 또 다른 작업 추가

```redis
LPUSH tasks "Task 2"
```

- **출력**: `(integer) 2`
- **설명**: "tasks" 리스트의 머리에 "Task 2" 추가, 리스트는 ["Task 2", "Task 1"].

### 리스트 요소 조회

```redis
LRANGE tasks 0 -1
```

- **출력**:
  ```
  1) "Task 2"
  2) "Task 1"
  ```
- **설명**: 리스트의 모든 요소 조회, 0부터 -1은 끝까지.

### 리스트 꼬리에 추가

```redis
RPUSH tasks "Task 3"
```

- **출력**: `(integer) 3`
- **설명**: "tasks" 리스트의 꼬리에 "Task 3" 추가.

### 리스트 머리에서 제거

```redis
LPOP tasks
```

- **출력**: `"Task 2"`
- **설명**: 리스트의 머리 요소 제거 및 반환.

**실무 예**: 작업 대기열 (`LPUSH job_queue "job1"`, `LPOP job_queue`).

## 세트 예제

세트는 중복 없는 문자열 집합입니다.

### 세트에 추가

```redis
SADD users "user1"
```

- **출력**: `(integer) 1`
- **설명**: "users" 세트에 "user1" 추가, 성공 시 1 반환.

### 또 다른 사용자 추가

```redis
SADD users "user2"
```

- **출력**: `(integer) 1`
- **설명**: "user2" 추가.

### 중복 추가 시도

```redis
SADD users "user1"
```

- **출력**: `(integer) 0`
- **설명**: "user1"은 이미 존재, 세트는 중복 허용 안 함.

### 모든 멤버 조회

```redis
SMEMBERS users
```

- **출력**:
  ```
  1) "user1"
  2) "user2"
  ```
- **설명**: 세트의 모든 멤버 조회.

### 멤버십 확인

```redis
SISMEMBER users "user1"
```

- **출력**: `(integer) 1`
- **설명**: "user1"이 세트에 있으면 1 반환.

### 비멤버 확인

```redis
SISMEMBER users "user3"
```

- **출력**: `(integer) 0`
- **설명**: "user3"이 없으면 0 반환.

**실무 예**: 고유 방문자 추적 (`SADD visitors "visitor1"`, `SCARD visitors`).

## 해시 예제

해시는 필드-값 매핑으로, 객체 저장에 적합합니다.

### 필드 설정

```redis
HSET user:1 name "Bob" age 25
```

- **출력**: `(integer) 2`
- **설명**: "user:1" 해시에 "name"과 "age" 필드 설정, 새 필드 수 반환.

### 필드 조회

```redis
HGET user:1 name
```

- **출력**: `"Bob"`
- **설명**: "name" 필드 값 조회.

### 모든 필드 조회

```redis
HGETALL user:1
```

- **출력**:
  ```
  1) "name"
  2) "Bob"
  3) "age"
  4) "25"
  ```
- **설명**: 모든 필드와 값 조회.

### 필드 값 증가

```redis
HINCRBY user:1 age 1
```

- **출력**: `(integer) 26`
- **설명**: "age" 필드 값을 1 증가.

**실무 예**: 사용자 프로필 저장 (`HSET user:1 name "Alice" email "alice@example.com"`).

## 정렬된 세트 예제

정렬된 세트는 점수를 기반으로 정렬된 멤버 집합입니다.

### 멤버 추가

```redis
ZADD leaderboard 100 "Player1"
```

- **출력**: `(integer) 1`
- **설명**: "leaderboard"에 "Player1" 멤버, 점수 100 추가.

### 추가 멤버

```redis
ZADD leaderboard 200 "Player2" 150 "Player3"
```

- **출력**: `(integer) 2`
- **설명**: "Player2"와 "Player3" 추가.

### 점수 오름차순 조회

```redis
ZRANGE leaderboard 0 -1 WITHSCORES
```

- **출력**:
  ```
  1) "Player1"
  2) "100"
  3) "Player3"
  4) "150"
  5) "Player2"
  6) "200"
  ```
- **설명**: 점수 오름차순으로 멤버와 점수 조회.

### 상위 멤버 조회

```redis
ZREVRANGE leaderboard 0 1 WITHSCORES
```

- **출력**:
  ```
  1) "Player2"
  2) "200"
  3) "Player3"
  4) "150"
  ```
- **설명**: 점수 내림차순으로 상위 2명 조회.

### 순위 확인

```redis
ZREVRANK leaderboard "Player1"
```

- **출력**: `(integer) 2`
- **설명**: "Player1"의 순위 반환(0부터, 실제 순위는 3).

**실무 예**: 게임 리더보드 (`ZADD leaderboard 100 "player1"`, `ZREVRANGE leaderboard 0 2`).

## Pub/Sub 예제

Pub/Sub은 실시간 메시징에 사용됩니다. 두 개의 Redis CLI 창이 필요합니다.

### 구독자 터미널

```redis
SUBSCRIBE channel1
```

- **출력**:
  ```
  1) "subscribe"
  2) "channel1"
  3) (integer) 1
  ```
- **설명**: "channel1" 채널 구독, 메시지 대기.

### 발행자 터미널

```redis
PUBLISH channel1 "Hello, subscriber!"
```

- **출력**: `(integer) 1`
- **설명**: "channel1"에 메시지 발행, 구독자 수 반환.

### 구독자 터미널에서 수신

- **출력**:
  ```
  1) "message"
  2) "channel1"
  3) "Hello, subscriber!"
  ```
- **설명**: 발행된 메시지 수신.

**실무 예**: 실시간 알림 시스템.

## 트랜잭션 예제

트랜잭션은 원자적 명령 실행을 보장합니다.

### 트랜잭션 시작

```redis
MULTI
```

- **출력**: `OK`
- **설명**: 트랜잭션 시작.

### 명령 대기

```redis
SET key1 "value1"
```

- **출력**: `QUEUED`
- **설명**: 명령이 대기 중.

### 또 다른 명령

```redis
SET key2 "value2"
```

- **출력**: `QUEUED`

### 트랜잭션 실행

```redis
EXEC
```

- **출력**:
  ```
  1) OK
  2) OK
  ```
- **설명**: 대기된 명령 실행, 성공 시 OK 반환.

### 값 확인

```redis
GET key1
```

- **출력**: `"value1"`
- **설명**: 값 조회.

**실무 예**: 사용자 잔액 업데이트와 로그 동시 처리.

## 실무 시나리오: 간단한 블로그 시스템

블로그 게시물 관리 예제입니다.

### 게시물 제목 설정

```redis
SET post:1:title "My First Post"
```

- **출력**: `OK`

### 게시물 내용 설정

```redis
SET post:1:content "This is the content of my first post."
```

- **출력**: `OK`

### 태그 추가

```redis
SADD post:1:tags "python"
```

- **출력**: `(integer) 1`

```redis
SADD post:1:tags "redis"
```

- **출력**: `(integer) 1`

### 댓글 추가

```redis
LPUSH post:1:comments "Great post!"
```

- **출력**: `(integer) 1`

```redis
LPUSH post:1:comments "Looking forward to more."
```

- **출력**: `(integer) 2`

### 데이터 조회

```redis
GET post:1:title
```

- **출력**: `"My First Post"`

```redis
SMEMBERS post:1:tags
```

- **출력**:
  ```
  1) "python"
  2) "redis"
  ```

```redis
LRANGE post:1:comments 0 -1
```

- **출력**:
  ```
  1) "Looking forward to more."
  2) "Great post!"
  ```

**실무 예**: 블로그 플랫폼에서 게시물, 태그, 댓글 관리.

## Windows 10/11 환경 고려사항

| 항목               | Windows 10                          | Windows 11                          |
|-------------------|-------------------------------------|-------------------------------------|
| WSL2 지원         | 2004 빌드 이상, 설정 복잡           | 기본 최적화, 설치 간단               |
| 네트워킹          | WSL2 IP 확인 필요 (`wsl hostname -I`) | localhost 안정적 연결               |
| Docker 관리       | CLI 중심                            | Docker Desktop GUI 간소화           |

- **Windows 10**: WSL2 사용 시 `localhost` 대신 WSL2 IP로 연결, `docker exec -it my-redis redis-cli`로 CLI 접속.
- **Windows 11**: `localhost:6379`로 안정적 연결, Docker Desktop GUI로 컨테이너 관리 간편.

## 참고 자료
- [Redis 공식 문서]([invalid url, do not cite])
- [Real Python: Redis 사용법]([invalid url, do not cite])
- [DEV Community: Redis 데이터셋]([invalid url, do not cite])