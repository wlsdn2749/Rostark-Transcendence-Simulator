# 로스트아크 초월 시뮬레이터
> 로스트아크의 [초월 시스템](https://lostark.game.onstove.com/GameGuide/Pages/초월#h4-3)의 시뮬레이터를 제작합니다.
> 시뮬레이터 전반적인 개발과 전략적 선택에 도움을 주는 시스템을 개발하고 웹으로 서비스하는 것을 목표로 두고 있습니다.



## ✅ 개발 상태
1. [ ] 초월 시스템 구축 **( 시뮬레이터 )**
   1. [ ] **석판**
        1. [x] 5x5 석판
        2. [ ] 6x6 석판
        3. [x] 석판 파괴
        4. [ ] 특수 석판 ( 신비 석판, 왜곡된 고대 석판)

   2. [ ] **정령**
        1. [ ] 일반 정령 ( 2 / 12 )
        2. [ ] 강화 정령 ( 0 / 12 )
        3. [ ] 전설 정령 ( 0 / 12 )
   3. [ ] **기타**
        1. [x] 다음 정령 슬롯, 정령 교체
        2. [ ] 초월 완료
2. [ ] 강화학습 환경 구축 **(Custom gym 환경 구축)**
   1. [ ] pygame -> custom gym env packing
3. [ ] 웹 서비스 **( Public Release )**
4. [ ] 강화학습 **( Sequential Decision Making )**
   1. [ ] Model-Based
   2. [ ] Model-Free


## ⚙️ 설치
윈도우 환경(WSL) 또는 리눅스 환경에서 실행해주시면 됩니다. (Requires Python 3.9 +):

Poetry 설치후
```
poetry install
```

파이썬 실행
```
python games/main.py
```

## 기여
**기여**는 언제나 환영입니다!
디스코드에 오셔서 정보 공유와 기여를 해주시면 감사하겠습니다
- [Discord](https://discord.gg/JNMe8kYP)
