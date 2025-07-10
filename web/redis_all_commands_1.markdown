# Redis CLI 모든 명령어 목록 및 예제

이 문서는 Redis CLI에서 사용할 수 있는 주요 명령어를 데이터 유형별로 정리하며, 각 명령어의 기능, 입력 예제, 출력, 실무적 맥락을 초보자도 이해할 수 있도록 설명합니다. Windows 10/11 환경에서 Docker로 실행된 Redis 서버를 기반으로 작성되었습니다.

## 시작하기

### redis-server
- **설명**: Redis 서버를 시작합니다.
- **예제**:
  ```bash
  redis-server
  ```
- **출력**: 서버 시작 메시지 (터미널에 로그 출력).
- **실무 예**: Redis 데이터베이스 실행.

### redis-cli
- **설명**: Redis CLI를 열어 서버와 상호작용합니다.
- **예제**:
  ```bash
  redis-cli
  ```
- **출력**: `127.0.0.1:6379>`
- **실무 예**: Redis 서버에 연결해 명령어 입력.

### PING
- **설명**: 서버가 실행 중인지 확인합니다.
- **예제**:
  ```redis
  PING
  ```
- **출력**: `PONG`
- **실무 예**: 서버 상태 점검.

## 문자열 명령어

### SET
- **설명**: 키에 문자열 값을 설정합니다.
- **예제**:
  ```redis
  SET mykey "Hello"
  ```
- **출력**: `OK`
- **실무 예**: 사용자 이름 저장.

### GET
- **설명**: 키의 값을 조회합니다.
- **예제**:
  ```redis
  GET mykey
  ```
- **출력**: `"Hello"`
- **실무 예**: 저장된 사용자 이름 조회.

### APPEND
- **설명**: 키의 값 끝에 문자열을 추가합니다.
- **예제**:
  ```redis
  APPEND mykey " World"
  ```
- **출력**: `(integer) 11`
- **실무 예**: 로그 메시지 추가.

### INCR
- **설명**: 키의 정수 값을 1 증가시킵니다.
- **예제**:
  ```redis
  SET counter 0
  INCR counter
  ```
- **출력**: `(integer) 1`
- **실무 예**: 페이지 조회수 증가.

### DECR
- **설명**: 키의 정수 값을 1 감소시킵니다.
- **예제**:
  ```redis
  DECR counter
  ```
- **출력**: `(integer) 0`
- **실무 예**: 재고 수량 감소.

### MSET
- **설명**: 여러 키에 값을 동시에 설정합니다.
- **예제**:
  ```redis
  MSET key1 "value1" key2 "value2"
  ```
- **출력**: `OK`
- **실무 예**: 다중 사용자 속성 저장.

### MGET
- **설명**: 여러 키의 값을 동시에 조회합니다.
- **예제**:
  ```redis
  MGET key1 key2
  ```
- **출력**:
  ```
  1) "value1"
  2) "value2"
  ```
- **실무 예**: 다중 사용자 속성 조회.

### SETEX
- **설명**: 키에 값을 설정하고 만료 시간을 지정합니다.
- **예제**:
  ```redis
  SETEX session 3600 "session_data"
  ```
- **출력**: `OK`
- **실무 예**: 사용자 세션 저장.

### PSETEX
- **설명**: 키에 값을 설정하고 밀리초 단위로 만료 시간을 지정합니다.
- **예제**:
  ```redis
  PSETEX temp 1000 "temp_data"
  ```
- **출력**: `OK`
- **실무 예**: 임시 데이터 저장.

### SETNX
- **설명**: 키가 존재하지 않을 때만 값을 설정합니다.
- **예제**:
  ```redis
  SETNX mykey "New"
  ```
- **출력**: `(integer) 0` (이미 존재)
- **실무 예**: 중복 방지.

### GETSET
- **설명**: 키의 값을 설정하고 이전 값을 반환합니다.
- **예제**:
  ```redis
  GETSET mykey "New Value"
  ```
- **출력**: `"Hello World"`
- **실무 예**: 값 업데이트 및 이전 값 확인.

### STRLEN
- **설명**: 키에 저장된 문자열의 길이를 반환합니다.
- **예제**:
  ```redis
  STRLEN mykey
  ```
- **출력**: `(integer) 9`
- **실무 예**: 데이터 크기 확인.

### INCRBY
- **설명**: 키의 정수 값을 지정된 값만큼 증가시킵니다.
- **예제**:
  ```redis
  INCRBY counter 10
  ```
- **출력**: `(integer) 10`
- **실무 예**: 점수 증가.

### DECRBY
- **설명**: 키의 정수 값을 지정된 값만큼 감소시킵니다.
- **예제**:
  ```redis
  DECRBY counter 5
  ```
- **출력**: `(integer) 5`
- **실무 예**: 재고 감소.

### INCRBYFLOAT
- **설명**: 키의 부동소수점 값을 증가시킵니다.
- **예제**:
  ```redis
  SET float 10.5
  INCRBYFLOAT float 0.5
  ```
- **출력**: `"11"`
- **실무 예**: 소수점 계산.

### GETRANGE
- **설명**: 키의 문자열 값에서 지정된 범위의 부분 문자열을 반환합니다.
- **예제**:
  ```redis
  GETRANGE mykey 0 4
  ```
- **출력**: `"New V"`
- **실무 예**: 문자열 일부 추출.

### SETRANGE
- **설명**: 키의 문자열 값을 지정된 오프셋부터 덮어씁니다.
- **예제**:
  ```redis
  SETRANGE mykey 5 "alue"
  ```
- **출력**: `(integer) 9`
- **실무 예**: 문자열 수정.

### BITCOUNT
- **설명**: 문자열의 설정된 비트 수를 계산합니다.
- **예제**:
  ```redis
  SET bitkey "foobar"
  BITCOUNT bitkey
  ```
- **출력**: `(integer) 26`
- **실무 예**: 비트 분석.

### BITOP
- **설명**: 여러 문자열에 비트 연산을 수행합니다.
- **예제**:
  ```redis
  BITOP AND result bitkey1 bitkey2
  ```
- **출력**: `(integer) 6`
- **실무 예**: 비트 집합 연산.

### BITPOS
- **설명**: 문자열에서 첫 번째 설정 또는 해제된 비트의 위치를 찾습니다.
- **예제**:
  ```redis
  BITPOS bitkey 1
  ```
- **출력**: `(integer) 1`
- **실무 예**: 비트 위치 탐색.

### GETBIT
- **설명**: 문자열의 특정 오프셋에서 비트 값을 반환합니다.
- **예제**:
  ```redis
  GETBIT bitkey 0
  ```
- **출력**: `(integer) 0`
- **실무 예**: 비트 상태 확인.

### SETBIT
- **설명**: 문자열의 특정 오프셋에 비트 값을 설정합니다.
- **예제**:
  ```redis
  SETBIT bitkey 0 1
  ```
- **출력**: `(integer) 0`
- **실무 예**: 비트 설정.

### BITFIELD
- **설명**: 문자열에 비트 필드 연산을 수행합니다.
- **예제**:
  ```redis
  BITFIELD mykey INCRBY i5 100 1
  ```
- **출력**: `1) (integer) 1`
- **실무 예**: 비트 단위 데이터 조작.

### STRALGO
- **설명**: 문자열에 대해 알고리즘(예: LCS)을 실행합니다.
- **예제**:
  ```redis
  STRALGO LCS KEYS key1 key2
  ```
- **출력**: (LCS 결과)
- **실무 예**: 문자열 비교.

## 리스트 명령어

### LPUSH
- **설명**: 리스트의 머리에 요소를 추가합니다.
- **예제**:
  ```redis
  LPUSH mylist "World"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 작업 대기열 추가.

### RPUSH
- **설명**: 리스트의 꼬리에 요소를 추가합니다.
- **예제**:
  ```redis
  RPUSH mylist "Hello"
  ```
- **출력**: `(integer) 2`
- **실무 예**: 로그 추가.

### LRANGE
- **설명**: 리스트의 지정된 범위 요소를 반환합니다.
- **예제**:
  ```redis
  LRANGE mylist 0 -1
  ```
- **출력**:
  ```
  1) "World"
  2) "Hello"
  ```
- **실무 예**: 작업 목록 조회.

### LLEN
- **설명**: 리스트의 길이를 반환합니다.
- **예제**:
  ```redis
  LLEN mylist
  ```
- **출력**: `(integer) 2`
- **실무 예**: 대기열 크기 확인.

### LPOP
- **설명**: 리스트의 머리 요소를 제거하고 반환합니다.
- **예제**:
  ```redis
  LPOP mylist
  ```
- **출력**: `"World"`
- **실무 예**: 작업 처리.

### RPOP
- **설명**: 리스트의 꼬리 요소를 제거하고 반환합니다.
- **예제**:
  ```redis
  RPOP mylist
  ```
- **출력**: `"Hello"`
- **실무 예**: 마지막 로그 제거.

### LINDEX
- **설명**: 리스트의 지정된 인덱스 요소를 반환합니다.
- **예제**:
  ```redis
  LPUSH mylist "World"
  LINDEX mylist 0
  ```
- **출력**: `"World"`
- **실무 예**: 특정 작업 조회.

### LINSERT
- **설명**: 리스트의 특정 요소 앞/뒤에 요소를 삽입합니다.
- **예제**:
  ```redis
  LINSERT mylist BEFORE "World" "Hello"
  ```
- **출력**: `(integer) 2`
- **실무 예**: 작업 순서 조정.

### LSET
- **설명**: 리스트의 지정된 인덱스 요소를 설정합니다.
- **예제**:
  ```redis
  LSET mylist 0 "New"
  ```
- **출력**: `OK`
- **실무 예**: 작업 업데이트.

### LREM
- **설명**: 리스트에서 지정된 요소를 제거합니다.
- **예제**:
  ```redis
  LREM mylist 1 "New"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 중복 작업 제거.

### LTRIM
- **설명**: 리스트를 지정된 범위로 자릅니다.
- **예제**:
  ```redis
  LTRIM mylist 0 1
  ```
- **출력**: `OK`
- **실무 예**: 로그 정리.

### RPOPLPUSH
- **설명**: 리스트의 꼬리 요소를 제거하고 다른 리스트의 머리에 추가합니다.
- **예제**:
  ```redis
  RPOPLPUSH mylist otherlist
  ```
- **출력**: `"World"`
- **실무 예**: 작업 이동.

### LMOVE
- **설명**: 리스트 간 요소를 이동합니다.
- **예제**:
  ```redis
  LMOVE mylist otherlist LEFT RIGHT
  ```
- **출력**: `"World"`
- **실무 예**: 작업 재배치.

### BLPOP
- **설명**: 리스트의 머리 요소를 제거하고 반환하거나, 요소가 있을 때까지 대기합니다.
- **예제**:
  ```redis
  BLPOP mylist 10
  ```
- **출력**: (요소 또는 nil)
- **실무 예**: 비동기 작업 처리.

### BRPOP
- **설명**: 리스트의 꼬리 요소를 제거하고 반환하거나, 대기합니다.
- **예제**:
  ```redis
  BRPOP mylist 10
  ```
- **출력**: (요소 또는 nil)
- **실무 예**: 메시지 큐 처리.

### LPUSHX
- **설명**: 리스트가 존재할 때만 머리에 요소를 추가합니다.
- **예제**:
  ```redis
  LPUSHX mylist "New"
  ```
- **출력**: `(integer) 0` (리스트 없음)
- **실무 예**: 안전한 추가.

### RPUSHX
- **설명**: 리스트가 존재할 때만 꼬리에 요소를 추가합니다.
- **예제**:
  ```redis
  RPUSHX mylist "New"
  ```
- **출력**: `(integer) 0`
- **실무 예**: 안전한 추가.

### LPOS
- **설명**: 리스트에서 요소의 인덱스를 반환합니다.
- **예제**:
  ```redis
  LPOS mylist "World"
  ```
- **출력**: `(integer) 0`
- **실무 예**: 작업 위치 확인.

## 세트 명령어

### SADD
- **설명**: 세트에 멤버를 추가합니다.
- **예제**:
  ```redis
  SADD myset "Hello"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 고유 사용자 추가.

### SMEMBERS
- **설명**: 세트의 모든 멤버를 반환합니다.
- **예제**:
  ```redis
  SMEMBERS myset
  ```
- **출력**:
  ```
  1) "Hello"
  ```
- **실무 예**: 사용자 목록 조회.

### SREM
- **설명**: 세트에서 멤버를 제거합니다.
- **예제**:
  ```redis
  SREM myset "Hello"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 사용자 삭제.

### SCARD
- **설명**: 세트의 멤버 수를 반환합니다.
- **예제**:
  ```redis
  SCARD myset
  ```
- **출력**: `(integer) 0`
- **실무 예**: 방문자 수 확인.

### SISMEMBER
- **설명**: 멤버가 세트에 있는지 확인합니다.
- **예제**:
  ```redis
  SISMEMBER myset "Hello"
  ```
- **출력**: `(integer) 0`
- **실무 예**: 사용자 존재 확인.

### SMISMEMBER
- **설명**: 여러 멤버의 존재 여부를 확인합니다.
- **예제**:
  ```redis
  SMISMEMBER myset "Hello" "World"
  ```
- **출력**:
  ```
  1) (integer) 0
  2) (integer) 0
  ```
- **실무 예**: 다중 사용자 확인.

### SINTER
- **설명**: 여러 세트의 교집합을 반환합니다.
- **예제**:
  ```redis
  SADD set1 "a" "b"
  SADD set2 "b" "c"
  SINTER set1 set2
  ```
- **출력**:
  ```
  1) "b"
  ```
- **실무 예**: 공통 사용자 찾기.

### SINTERSTORE
- **설명**: 교집합을 새 세트에 저장합니다.
- **예제**:
  ```redis
  SINTERSTORE result set1 set2
  ```
- **출력**: `(integer) 1`
- **실무 예**: 공통 데이터 저장.

### SUNION
- **설명**: 여러 세트의 합집합을 반환합니다.
- **예제**:
  ```redis
  SUNION set1 set2
  ```
- **출력**:
  ```
  1) "a"
  2) "b"
  3) "c"
  ```
- **실무 예**: 전체 사용자 목록.

### SUNIONSTORE
- **설명**: 합집합을 새 세트에 저장합니다.
- **예제**:
  ```redis
  SUNIONSTORE result set1 set2
  ```
- **출력**: `(integer) 3`
- **실무 예**: 데이터 통합.

### SDIFF
- **설명**: 세트 간 차집합을 반환합니다.
- **예제**:
  ```redis
  SDIFF set1 set2
  ```
- **출력**:
  ```
  1) "a"
  ```
- **실무 예**: 고유 사용자 찾기.

### SDIFFSTORE
- **설명**: 차집합을 새 세트에 저장합니다.
- **예제**:
  ```redis
  SDIFFSTORE result set1 set2
  ```
- **출력**: `(integer) 1`
- **실무 예**: 고유 데이터 저장.

### SPOP
- **설명**: 세트에서 무작위 멤버를 제거하고 반환합니다.
- **예제**:
  ```redis
  SPOP myset
  ```
- **출력**: `"Hello"`
- **실무 예**: 랜덤 사용자 선택.

### SRANDMEMBER
- **설명**: 세트에서 무작위 멤버를 반환합니다.
- **예제**:
  ```redis
  SRANDMEMBER myset
  ```
- **출력**: `"Hello"`
- **실무 예**: 랜덤 추천.

### SMOVE
- **설명**: 세트 간 멤버를 이동합니다.
- **예제**:
  ```redis
  SMOVE set1 set2 "a"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 사용자 그룹 변경.

## 해시 명령어

### HSET
- **설명**: 해시 필드에 값을 설정합니다.
- **예제**:
  ```redis
  HSET myhash field1 "value1"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 사용자 프로필 저장.

### HGET
- **설명**: 해시 필드의 값을 조회합니다.
- **예제**:
  ```redis
  HGET myhash field1
  ```
- **출력**: `"value1"`
- **실무 예**: 프로필 속성 조회.

### HMSET
- **설명**: 여러 해시 필드에 값을 설정합니다.
- **예제**:
  ```redis
  HMSET myhash field1 "value1" field2 "value2"
  ```
- **출력**: `OK`
- **실무 예**: 다중 속성 저장.

### HGETALL
- **설명**: 해시의 모든 필드와 값을 반환합니다.
- **예제**:
  ```redis
  HGETALL myhash
  ```
- **출력**:
  ```
  1) "field1"
  2) "value1"
  3) "field2"
  4) "value2"
  ```
- **실무 예**: 전체 프로필 조회.

### HMGET
- **설명**: 여러 해시 필드의 값을 조회합니다.
- **예제**:
  ```redis
  HMGET myhash field1 field2
  ```
- **출력**:
  ```
  1) "value1"
  2) "value2"
  ```
- **실무 예**: 선택적 속성 조회.

### HINCRBY
- **설명**: 해시 필드의 정수 값을 증가시킵니다.
- **예제**:
  ```redis
  HINCRBY myhash points 10
  ```
- **출력**: `(integer) 10`
- **실무 예**: 사용자 포인트 증가.

### HDEL
- **설명**: 해시에서 필드를 삭제합니다.
- **예제**:
  ```redis
  HDEL myhash field1
  ```
- **출력**: `(integer) 1`
- **실무 예**: 속성 제거.

### HLEN
- **설명**: 해시의 필드 수를 반환합니다.
- **예제**:
  ```redis
  HLEN myhash
  ```
- **출력**: `(integer) 1`
- **실무 예**: 프로필 크기 확인.

### HKEYS
- **설명**: 해시의 모든 필드 이름을 반환합니다.
- **예제**:
  ```redis
  HKEYS myhash
  ```
- **출력**:
  ```
  1) "field2"
  ```
- **실무 예**: 속성 목록 조회.

### HVALS
- **설명**: 해시의 모든 필드 값을 반환합니다.
- **예제**:
  ```redis
  HVALS myhash
  ```
- **출력**:
  ```
  1) "value2"
  ```
- **실무 예**: 값 목록 조회.

### HEXISTS
- **설명**: 해시 필드가 존재하는지 확인합니다.
- **예제**:
  ```redis
  HEXISTS myhash field2
  ```
- **출력**: `(integer) 1`
- **실무 예**: 속성 존재 확인.

## 정렬된 세트 명령어

### ZADD
- **설명**: 정렬된 세트에 멤버와 점수를 추가합니다.
- **예제**:
  ```redis
  ZADD myzset 1 "one"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 리더보드 점수 추가.

### ZRANGE
- **설명**: 정렬된 세트의 지정된 범위 멤버를 반환합니다.
- **예제**:
  ```redis
  ZRANGE myzset 0 -1 WITHSCORES
  ```
- **출력**:
  ```
  1) "one"
  2) "1"
  ```
- **실무 예**: 순위 조회.

### ZREVRANGE
- **설명**: 점수 내림차순으로 범위 멤버를 반환합니다.
- **예제**:
  ```redis
  ZREVRANGE myzset 0 1 WITHSCORES
  ```
- **출력**:
  ```
  1) "one"
  2) "1"
  ```
- **실무 예**: 상위 순위 조회.

### ZRANK
- **설명**: 멤버의 순위를 반환합니다.
- **예제**:
  ```redis
  ZRANK myzset "one"
  ```
- **출력**: `(integer) 0`
- **실무 예**: 사용자 순위 확인.

### ZREVRANK
- **설명**: 점수 내림차순으로 순위를 반환합니다.
- **예제**:
  ```redis
  ZREVRANK myzset "one"
  ```
- **출력**: `(integer) 0`
- **실무 예**: 상위 순위 확인.

### ZREM
- **설명**: 정렬된 세트에서 멤버를 제거합니다.
- **예제**:
  ```redis
  ZREM myzset "one"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 플레이어 제거.

### ZCARD
- **설명**: 정렬된 세트의 멤버 수를 반환합니다.
- **예제**:
  ```redis
  ZCARD myzset
  ```
- **출력**: `(integer) 0`
- **실무 예**: 리더보드 크기 확인.

### ZSCORE
- **설명**: 멤버의 점수를 반환합니다.
- **예제**:
  ```redis
  ZSCORE myzset "one"
  ```
- **출력**: `"1"`
- **실무 예**: 점수 조회.

### ZINCRBY
- **설명**: 멤버의 점수를 증가시킵니다.
- **예제**:
  ```redis
  ZINCRBY myzset 10 "one"
  ```
- **출력**: `"11"`
- **실무 예**: 점수 업데이트.

### ZRANGEBYSCORE
- **설명**: 점수 범위 내 멤버를 반환합니다.
- **예제**:
  ```redis
  ZRANGEBYSCORE myzset 0 100
  ```
- **출력**:
  ```
  1) "one"
  ```
- **실무 예**: 점수 필터링.

## Pub/Sub 명령어

### PUBLISH
- **설명**: 채널에 메시지를 발행합니다.
- **예제**:
  ```redis
  PUBLISH mychannel "Hello"
  ```
- **출력**: `(integer) 1`
- **실무 예**: 알림 발송.

### SUBSCRIBE
- **설명**: 채널