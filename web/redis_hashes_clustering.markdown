# Redis 해시와 클러스터링: 상세 가이드

이 문서는 Redis의 해시와 클러스터링에 대한 자세한 설명과 실습 예제를 제공합니다. 초보자를 위해 각 기능의 개념, 명령어, 예제, 출력, 실무적 맥락을 포함하며, Windows 10/11 환경에서 Docker로 실행된 Redis 서버를 기반으로 작성되었습니다. Redis CLI를 사용한 예제와 실무 시나리오를 통해 학습을 지원합니다.

## 1. Redis 해시

### 소개
Redis 해시는 단일 키 아래 여러 필드-값 쌍을 저장하는 데이터 구조로, 객체를 표현하거나 데이터를 효율적으로 관리하는 데 적합합니다. 예를 들어, 사용자 프로필을 하나의 키에 이름, 나이, 이메일 등의 필드로 저장할 수 있습니다. 해시는 메모리 효율적이며, 최대 2^32-1(약 42억)개의 필드-값 쌍을 저장할 수 있습니다.

### 기본 명령어

#### HSET
- **설명**: 해시의 필드에 값을 설정합니다. 키가 없으면 새 해시를 생성합니다.
- **구문**: `HSET key field value [field value ...]`
- **예제**:
  ```redis
  HSET user:1 name "Alice" age 30 email "alice@example.com"
  ```
  - **출력**: `(integer) 3`
  - **설명**: "user:1" 해시에 "name", "age", "email" 필드를 설정, 새 필드 수(3) 반환.
- **실무 예**: 사용자 프로필 저장.

#### HGET
- **설명**: 해시의 특정 필드 값을 조회합니다.
- **구문**: `HGET key field`
- **예제**:
  ```redis
  HGET user:1 name
  ```
  - **출력**: `"Alice"`
  - **설명**: "user:1" 해시의 "name" 필드 값 조회.
- **실무 예**: 사용자 이름 조회.

#### HGETALL
- **설명**: 해시의 모든 필드와 값을 반환합니다.
- **구문**: `HGETALL key`
- **예제**:
  ```redis
  HGETALL user:1
  ```
  - **출력**:
    ```
    1) "name"
    2) "Alice"
    3) "age"
    4) "30"
    5) "email"
    6) "alice@example.com"
    ```
  - **설명**: "user:1" 해시의 모든 필드와 값 반환.
- **실무 예**: 사용자 프로필 전체 조회.

#### HDEL
- **설명**: 해시에서 지정된 필드를 삭제합니다.
- **구문**: `HDEL key field [field ...]`
- **예제**:
  ```redis
  HDEL user:1 email
  ```
  - **출력**: `(integer) 1`
  - **설명**: "user:1" 해시에서 "email" 필드 삭제, 삭제된 필드 수 반환.
- **실무 예**: 불필요한 사용자 속성 제거.

#### HEXISTS
- **설명**: 해시에서 필드가 존재하는지 확인합니다.
- **구문**: `HEXISTS key field`
- **예je**:
  ```redis
  HEXISTS user:1 age
  ```
  - **출력**: `(integer) 1`
  - **설명**: "age" 필드가 존재하면 1, 없으면 0 반환.
- **실무 예**: 사용자 속성 존재 확인.

#### HMSET (레거시)
- **설명**: 여러 필드-값 쌍을 설정합니다 (Redis 4.0.0 이후 HSET으로 통합).
- **구문**: `HMSET key field value [field value ...]`
- **예제**:
  ```redis
  HMSET user:2 name "Bob" age 25
  ```
  - **출력**: `OK`
  - **설명**: "user:2" 해시에 여러 필드 설정.
- **실무 예**: 다중 사용자 속성 저장.

#### HMGET
- **설명**: 여러 필드의 값을 조회합니다.
- **구문**: `HMGET key field [field ...]`
- **예제**:
  ```redis
  HMGET user:1 name age
  ```
  - **출력**:
    ```
    1) "Alice"
    2) "30"
    ```
  - **설명**: "name"과 "age" 필드 값 반환.
- **실무 예**: 선택적 속성 조회.

#### HINCRBY
- **설명**: 필드의 정수 값을 증가시킵니다.
- **구문**: `HINCRBY key field increment`
- **예제**:
  ```redis
  HSET user:1 points 100
  HINCRBY user:1 points 10
  ```
  - **출력**: `(integer) 110`
  - **설명**: "points" 필드 값을 10 증가.
- **실무 예**: 사용자 포인트 증가.

#### HLEN
- **설명**: 해시의 필드 수를 반환합니다.
- **구문**: `HLEN key`
- **예제**:
  ```redis
  HLEN user:1
  ```
  - **출력**: `(integer) 2`
  - **설명**: "user:1" 해시의 필드 수 반환.
- **실무 예**: 프로필 크기 확인.

#### HKEYS
- **설명**: 해시의 모든 필드 이름을 반환합니다.
- **구문**: `HKEYS key`
- **예제**:
  ```redis
  HKEYS user:1
  ```
  - **출력**:
    ```
    1) "name"
    2) "age"
    ```
  - **설명**: "user:1" 해시의 필드 이름 목록 반환.
- **실무 예**: 속성 목록 조회.

#### HVALS
- **설명**: 해시의 모든 필드 값을 반환합니다.
- **구문**: `HVALS key`
- **예je**:
  ```redis
  HVALS user:1
  ```
  - **출력**:
    ```
    1) "Alice"
    2) "30"
    ```
  - **설명**: "user:1" 해시의 필드 값 목록 반환.
- **실무 예**: 값 목록 조회.

### 고급 기능
Redis 7.4부터 필드별 만료 시간(TTL)을 설정할 수 있습니다. 이는 이벤트 추적이나 세션 관리에 유용합니다.

#### HEXPIRE
- **설명**: 필드에 만료 시간을 설정합니다(초 단위).
- **구문**: `HEXPIRE key seconds field [field ...]`
- **예제**:
  ```redis
  HEXPIRE user:1 3600 session_token
  ```
  - **출력**: `(integer) 1`
  - **설명**: "session_token" 필드에 3600초(1시간) 만료 시간 설정.
- **실무 예**: 사용자 세션 자동 삭제.

#### HTTL
- **설명**: 필드의 남은 만료 시간을 반환합니다.
- **구문**: `HTTL key field`
- **예제**:
  ```redis
  HTTL user:1 session_token
  ```
  - **출력**: `(integer) 3600`
  - **설명**: "session_token" 필드의 남은 만료 시간 반환.
- **실무 예**: 세션 유효 기간 확인.

### 사용 사례
- **사용자 프로필**: 이름, 나이, 이메일 등을 단일 키에 저장.
- **설정 관리**: 애플리케이션 설정을 필드-값 쌍으로 저장.
- **이벤트 추적**: 시간 제한이 있는 이벤트를 필드별 TTL로 관리.
- **세션 관리**: 세션 데이터를 필드별 만료로 관리.

### 성능 고려사항
- 대부분의 해시 명령어는 O(1) 시간 복잡도를 가지며 효율적입니다.
- `HGETALL`, `HKEYS`, `HVALS`는 O(n) 복잡도를 가지므로 대규모 해시에서 주의해야 합니다.
- 최대 2^32-1(약 42억) 필드-값 쌍을 저장 가능, 메모리 제한에 주의.

## 2. Redis 클러스터링

### 소개
Redis 클러스터링은 데이터를 여러 노드에 분산 저장하여 확장성과 고가용성을 제공합니다. 데이터는 16384개의 해시 슬롯으로 나뉘며, 각 키는 해시 함수를 통해 슬롯에 매핑됩니다. 이는 대규모 데이터 처리와 장애 복구에 유용합니다.

### 기본 개념
- **노드**: 클러스터를 구성하는 개별 Redis 인스턴스.
- **슬롯**: 데이터는 16384개의 해시 슬롯으로 분할, 각 키는 CRC16 해시로 슬롯에 매핑.
- **마스터와 레플리카**: 마스터 노드는 슬롯의 일부를 담당, 레플리카는 데이터 복제를 제공.

### 클러스터 설정
최소 3개의 마스터 노드가 필요하며, 고가용성을 위해 각 마스터당 최소 1개의 레플리카를 권장합니다.

#### 설정 파일
각 노드의 `redis.conf`:
```
port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
```

#### 클러스터 생성
```bash
redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 --cluster-replicas 0
```
- **설명**: 3개의 마스터 노드로 클러스터 생성, 레플리카 없음.

#### 레플리카 추가
```bash
redis-cli --cluster add-node 127.0.0.1:7003 127.0.0.1:7000 --cluster-slave
```
- **설명**: 새 노드를 레플리카로 추가.

### 클러스터와 상호작용
클러스터 모드에서 `redis-cli` 사용:
```bash
redis-cli -c -p 7000
```
- `-c`: 클러스터 모드 활성화, 키의 슬롯에 따라 명령어를 자동 라우팅.

#### 예제: 데이터 저장 및 조회
```redis
SET mykey "Hello, Cluster!"
```
- **출력**: `OK`
- **설명**: 클러스터가 키를 적절한 노드에 저장.

```redis
GET mykey
```
- **출력**: `"Hello, Cluster!"`
- **설명**: 클러스터가 키를 적절한 노드에서 조회.

### 해시 태그
여러 키를 동일 노드에 저장하려면 해시 태그(`{}`)를 사용합니다.

#### 예제: 해시 태그 사용
```redis
SET {user:1}:name "Alice"
SET {user:1}:age 30
```
- **설명**: `{user:1}` 해시 태그로 두 키가 동일 슬롯에 저장.
- **실무 예**: 트랜잭션에서 여러 키를 동시에 처리.

#### 예제: 다중 키 조회
```redis
MGET {user:1}:name {user:1}:age
```
- **출력**:
  ```
  1) "Alice"
  2) "30"
  ```
- **설명**: 동일 슬롯에 있는 키를 조회.

### 사용 사례
- **대규모 데이터 처리**: 데이터를 여러 노드에 분배해 처리량 증가.
- **고가용성**: 마스터 장애 시 레플리카가 자동 승격.
- **실시간 애플리케이션**: 채팅, 알림 시스템에서 빠른 데이터 처리.

### 성능 고려사항
- 클러스터는 비동기 복제를 사용하므로 장애 시 소량의 쓰기 손실 가능.
- 다중 키 명령어는 동일 슬롯에 있어야 하며, 해시 태그로 관리.
- `CLUSTER INFO`로 클러스터 상태 확인:
  ```redis
  CLUSTER INFO
  ```
  - 출력: 클러스터 상태 정보.

## 3. 실행 환경
- **Docker 실행**:
  ```bash
  docker run -d -p 6379:6379 --name my-redis redis:latest
  ```
- **Redis CLI 접속**:
  ```bash
  docker exec -it my-redis redis-cli
  ```
- **Windows 환경**:
  - Windows 10: WSL2 IP 확인(`wsl hostname -I`) 필요.
  - Windows 11: `localhost:6379`로 안정적 연결, Docker Desktop GUI 활용.

## 4. 참고 자료
- [Redis 공식 문서](https://redis.io/docs/)
- [Redis 해시 문서](https://redis.io/docs/latest/develop/data-types/hashes/)
- [Redis 클러스터 문서](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)