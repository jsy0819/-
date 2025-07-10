# Redis Pub/Sub 명령어: 실습 중심 가이드

이 문서는 Redis CLI에서 사용할 수 있는 Pub/Sub 명령어를 상세히 설명하며, 초보자를 위해 각 명령어의 기능, 구문, 실습 예제, 실무적 맥락을 제공합니다. Windows 10/11 환경에서 Docker로 실행된 Redis 서버를 기반으로 작성되었으며, 간단한 채팅 시스템을 중심으로 실습 가능한 예제를 포함합니다.

## Pub/Sub 소개

Redis의 Pub/Sub(Publish/Subscribe)은 발행자(Publisher)가 채널에 메시지를 보내고, 구독자(Subscriber)가 해당 채널에서 메시지를 받는 메시징 패턴입니다. 발행자와 구독자는 서로를 알 필요 없이 채널을 통해 통신하며, 이는 실시간 채팅, 알림 시스템, 이벤트 기반 아키텍처에 유용합니다. Redis Pub/Sub는 다음과 같은 특징을 가집니다:
- **비영속성**: 메시지는 저장되지 않으며, 구독자가 연결되지 않은 동안의 메시지는 손실됩니다.
- **최대 한 번 전달**: 메시지는 최대 한 번만 전달되며, 재전송되지 않습니다.
- **데이터베이스 독립성**: 채널은 Redis 데이터베이스와 무관하게 전역적으로 작동합니다.

## Pub/Sub 명령어

### 1. SUBSCRIBE
- **설명**: 클라이언트를 지정된 채널에 구독시켜 해당 채널에 발행된 모든 메시지를 수신합니다. 구독 모드에서는 다른 명령어 입력이 제한됩니다(단, RESP3 프로토콜에서는 예외).
- **구문**: `SUBSCRIBE channel [channel ...]`
- **예제**:
  ```redis
  SUBSCRIBE chatroom
  ```
  - **출력**:
    ```
    1) "subscribe"
    2) "chatroom"
    3) (integer) 1
    ```
  - **설명**: "chatroom" 채널을 구독, 메시지 대기 시작. 출력은 구독 성공 메시지로, 세 번째 요소는 현재 구독 중인 채널 수(1)를 나타냄.
- **예제 2**: 여러 채널 구독
  ```redis
  SUBSCRIBE news alerts
  ```
  - **출력**:
    ```
    1) "subscribe"
    2) "news"
    3) (integer) 1
    1) "subscribe"
    2) "alerts"
    3) (integer) 2
    ```
  - **설명**: "news"와 "alerts" 채널을 구독, 구독 수는 2로 증가.
- **실무 예**: 실시간 채팅 앱에서 사용자가 특정 채팅방에 참여.

### 2. UNSUBSCRIBE
- **설명**: 클라이언트를 지정된 채널에서 구독 해제합니다. 채널을 지정하지 않으면 모든 채널에서 구독 해제됩니다. redis-cli에서는 구독 모드에서 직접 실행 불가하며, Ctrl-C로 종료해야 합니다.
- **구문**: `UNSUBSCRIBE [channel [channel ...]]`
- **예제**:
  ```redis
  UNSUBSCRIBE chatroom
  ```
  - **출력**:
    ```
    1) "unsubscribe"
    2) "chatroom"
    3) (integer) 0
    ```
  - **설명**: "chatroom" 채널 구독 해제, 구독 수는 0으로 감소.
- **예제 2**: 모든 채널 구독 해제
  ```redis
  UNSUBSCRIBE
  ```
  - **출력**:
    ```
    1) "unsubscribe"
    2) (nil)
    3) (integer) 0
    ```
  - **설명**: 모든 채널에서 구독 해제.
- **실무 예**: 사용자가 채팅방을 나갈 때.

### 3. PUBLISH
- **설명**: 지정된 채널에 메시지를 발행하여 모든 구독자에게 전달합니다. 반환 값은 메시지를 받은 구독자 수입니다.
- **구문**: `PUBLISH channel message`
- **예제**:
  ```redis
  PUBLISH chatroom "Hello, everyone!"
  ```
  - **출력**: `(integer) 2`
  - **설명**: "chatroom" 채널에 "Hello, everyone!" 메시지를 발행, 2명의 구독자에게 전달.
- **예제 2**: JSON 메시지 발행
  ```redis
  PUBLISH notifications "{\"user\": \"Alice\", \"message\": \"New post!\"}"
  ```
  - **출력**: `(integer) 3`
  - **설명**: "notifications" 채널에 JSON 형식 메시지 발행, 3명의 구독자에게 전달.
- **실무 예**: 새 게시물 알림 발송.

### 4. PSUBSCRIBE
- **설명**: 지정된 패턴에 일치하는 모든 채널을 구독합니다. 와일드카드(*)를 사용해 여러 채널을 동시에 구독 가능.
- **구문**: `PSUBSCRIBE pattern [pattern ...]`
- **예제**:
  ```redis
  PSUBSCRIBE news.*
  ```
  - **출력**:
    ```
    1) "psubscribe"
    2) "news.*"
    3) (integer) 1
    ```
  - **설명**: "news.sports", "news.politics" 등 "news."로 시작하는 모든 채널 구독.
- **예제 2**: 메시지 수신
  - 발행자 터미널에서:
    ```redis
    PUBLISH news.sports "Football match update"
    ```
  - 구독자 터미널에서:
    ```
    1) "pmessage"
    2) "news.*"
    3) "news.sports"
    4) "Football match update"
    ```
  - **설명**: 패턴에 일치하는 채널의 메시지 수신, "pmessage"는 패턴 메시지임을 나타냄.
- **실무 예**: 뉴스 앱에서 카테고리별 알림 수신.

### 5. PUNSUBSCRIBE
- **설명**: 지정된 패턴에 일치하는 채널 구독을 해제합니다.
- **구문**: `PUNSUBSCRIBE [pattern [pattern ...]]`
- **예제**:
  ```redis
  PUNSUBSCRIBE news.*
  ```
  - **출력**:
    ```
    1) "punsubscribe"
    2) "news.*"
    3) (integer) 0
    ```
  - **설명**: "news.*" 패턴 구독 해제.
- **실무 예**: 뉴스 카테고리 알림 비활성화.

### 6. PUBSUB
- **설명**: Pub/Sub 시스템 상태를 검사하는 명령어로, 하위 명령어(CHANNELS, NUMSUB, NUMPAT)를 포함합니다.
- **구문**:
  - `PUBSUB CHANNELS [pattern]`: 활성 채널 목록 반환.
  - `PUBSUB NUMSUB [channel ...]`: 지정된 채널의 구독자 수 반환.
  - `PUBSUB NUMPAT`: 패턴 구독 수 반환.
- **예제 1**: 활성 채널 목록
  ```redis
  PUBSUB CHANNELS
  ```
  - **출력**:
    ```
    1) "chatroom"
    2) "news.sports"
    ```
  - **설명**: 현재 활성 채널 목록 반환.
- **예제 2**: 채널 구독자 수
  ```redis
  PUBSUB NUMSUB chatroom
  ```
  - **출력**:
    ```
    1) "chatroom"
    2) (integer) 2
    ```
  - **설명**: "chatroom" 채널의 구독자 수(2) 반환.
- **예제 3**: 패턴 구독 수
  ```redis
  PUBSUB NUMPAT
  ```
  - **출력**: `(integer) 1`
  - **설명**: 현재 패턴 구독 수(1) 반환.
- **실무 예**: 시스템 모니터링, 채널 상태 점검.

## 실습 시나리오: 간단한 채팅 시스템

간단한 채팅 시스템을 통해 Pub/Sub 명령어를 실습해 봅시다.

1. **환경 설정**:
   - Docker로 Redis 실행:
     ```bash
     docker run -d -p 6379:6379 --name my-redis redis:latest
     ```
   - 세 개의 터미널을 열고 Redis CLI 접속:
     ```bash
     docker exec -it my-redis redis-cli
     ```

2. **구독자 설정**:
   - 터미널 1:
     ```redis
     SUBSCRIBE chatroom
     ```
     - 출력:
       ```
       1) "subscribe"
       2) "chatroom"
       3) (integer) 1
       ```
   - 터미널 2:
     ```redis
     SUBSCRIBE chatroom
     ```
     - 출력:
       ```
       1) "subscribe"
       2) "chatroom"
       3) (integer) 2
       ```

3. **메시지 발행**:
   - 터미널 3:
     ```redis
     PUBLISH chatroom "Hello, everyone!"
     ```
     - 출력: `(integer) 2`
   - 터미널 1과 2에서 수신:
     ```
     1) "message"
     2) "chatroom"
     3) "Hello, everyone!"
     ```
   - 추가 메시지 발행:
     ```redis
     PUBLISH chatroom "How are you?"
     ```
     - 출력: `(integer) 2`
     - 터미널 1과 2에서 수신:
       ```
       1) "message"
       2) "chatroom"
       3) "How are you?"
       ```

4. **패턴 구독**:
   - 터미널 2에서 Ctrl-C로 구독 종료 후:
     ```redis
     PSUBSCRIBE room.*
     ```
     - 출력:
       ```
       1) "psubscribe"
       2) "room.*"
       3) (integer) 1
       ```
   - 터미널 3:
     ```redis
     PUBLISH room.lobby "Welcome to the lobby!"
     ```
     - 터미널 2에서 수신:
       ```
       1) "pmessage"
       2) "room.*"
       3) "room.lobby"
       4) "Welcome to the lobby!"
       ```

5. **상태 확인**:
   - 터미널 3:
     ```redis
     PUBSUB CHANNELS
     ```
     - 출력:
       ```
       1) "chatroom"
       2) "room.lobby"
       ```
     ```redis
     PUBSUB NUMSUB chatroom
     ```
     - 출력:
       ```
       1) "chatroom"
       2) (integer) 1
       ```

## 추가 참고 사항

- **메시지 형식**:
  - `SUBSCRIBE`: "subscribe", 채널 이름, 구독 수.
  - `PUBLISH`: 구독자에게 "message", 채널 이름, 메시지 내용 전달.
  - `PSUBSCRIBE`: "psubscribe", 패턴, 구독 수.
  - `PUNSUBSCRIBE`: "punsubscribe", 패턴, 구독 수.

- **전달 보장**: Redis Pub/Sub는 최대 한 번 전달(at-most-once) 방식을 사용하며, 구독자가 연결되지 않은 동안의 메시지는 손실됩니다. 더 강력한 전달 보장이 필요하면 Redis Streams를 고려하세요.

- **비영속성**: 메시지는 Redis에 저장되지 않으며, 현재 구독자에게만 전달됩니다.

- **redis-cli 제한**: 구독 모드에서는 `UNSUBSCRIBE`나 `PUNSUBSCRIBE`를 직접 실행할 수 없으며, Ctrl-C로 종료해야 합니다.

- **Windows 환경**:
  - Windows 10: WSL2 IP 확인(`wsl hostname -I`) 필요, 방화벽 포트 6379 개방.
  - Windows 11: `localhost:6379`로 안정적 연결, Docker Desktop GUI 활용.

## 참고 자료
- [Redis 공식 문서](https://redis.io/docs/latest/develop/interact/pubsub/)
- [Redis Pub/Sub 튜토리얼 (Medium)](https://medium.com/redis-with-raphael-de-lio/understanding-pub-sub-in-redis-18278440c2a9)
- [Redis Pub/Sub 튜토리얼 (TutorialsPoint)](https://www.tutorialspoint.com/redis/redis_pub_sub.htm)