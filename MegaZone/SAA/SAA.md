# SAA 핵심 요약

1. Posix, NFS -> EFS
2. 고성능 posix -> Fsx for lustre
3. DynamoDB -> NoSQL, 키-값 페어, 문서 데이터베이스,중요하고 범용적이 쿼리 빠르고 저렴, 정형 또는 반정형 데이터 관리, AutoScaling, EC2연동 비효율적
4. Aurora -> 관계형 데이터베이스 , OLTP트랜잭션 워크로드 (관계형 데이터베이스 필요), Serverless -> 자동 스케일링 구성 
5. 인메모리 데이터베이스 -> ElasticCache Redis, DynamoDB Accelerator(DAX)
6. NLB -> 최고의 성능과 고정 IP / ALB -> 유연한 애플리케이션 관리 및 TLS 종료
7. Kinesis Data Firehose -> 서버리스, 데이터 분석 도구 쉽고 안정적으로 로드
8. Kinesis Data Stream ->  대규모 데이터 레코드 스트림 실시간 수집 처리, 데이터 하루부터 7일까지 보관, 클릭스트림
9. Kinesis Data Analytics -> 스트림 및 파이어호스와 함께 즉석 데이터 분석, 데이터 외부로 전송
10. VPC 공유 -> 한개 이상 서브넷 공유
11. Snowball edge-> 인터넷보다 빠른데 자동화 안됨
12. 다중 AZ -> 동기식 복제, 최소 두개의 가용 영역, 자동 장애 복구 
13. 읽기 전용 복제본 -> 비동기식 복제, 단일 리전, 장애 시 수동으로 승격
14. EMR -> 빅데이터 플랫폼
15. ETL -> Glue, 파티션 배치 그룹
16. Athena -> S3에서 표준 SQL을 사용하여 데이터 쉽게 분석 대화형 쿼리, 서버리스, 정형 반정형데이터 분석 
17. Pilot Light -> DR
18. 사용자 API -> X RAY
19. Neptune -> 그래프
20. Global Accelerator -> 글로벌 사용자 도움되는 네트워크 서비스, 특정 ip 및 고정 ip, 게임, IoT, Cloudfront랑 둘다 쉴드 가능
