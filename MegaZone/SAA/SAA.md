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
21. Amazon Neptune -> Amazon Neptune은 고도로 연결된 데이터 세트와 함께 작동하는 애플리케이션을 쉽게 구축하고 실행할 수 있는 빠르고 안정적인 완전 관리형 그래프 데이터베이스 서비스
22. Amazon Neptune은 대규모 사용자 프로필 및 상호 작용 세트를 빠르고 쉽게 처리하여 소셜 네트워킹 애플리케이션을 구축할 수 있습니다. Neptune을 사용하면 처리량이 높은 대화형 그래프 쿼리를 통해 소셜 기능을 애플리케이션에 가져올 수 있습니다. 예를 들어, 애플리케이션에 소셜 피드를 구축하는 경우 Neptune을 사용하여 사용자에게 그들의 가족이나 친구들의 업데이트 중 ‘좋아요’를 한 최근 업데이트와 가까이 사는 친구들의 업데이트를 우선적으로 제공할 수 있습니다.
23. Aurora 
- 내장 캐시 없으므로 ElasticCache 사용
- 읽기복제본을 설정하고 적절한 엔드포인트를 사용
- 장애 조치 우선 순위 지정

24. AWS X-Ray -> 개발자가 마이크로서비스 아키텍처를 사용하여 구축한 것과 같은 프로덕션, 분산 애플리케이션을 분석하고 디버그
25. AWS OpsWorks - Chef, Puppet
26. S3 웹 사이트 엔드포인트
- s3-website 대시(-) 리전 ‐ http://bucket-name.s3-website-Region.amazonaws.com
- s3-website 점(.) 리전 ‐ http://bucket-name.s3-website.Region.amazonaws.com

27. RDS 확장 모니터링
- RDS child process
- RDS processes
- OS processes
