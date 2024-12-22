# AI-Makerthon 팀 프로젝트 소개

## 목차
- [팀 소개](#팀-소개)
- [프로젝트 개발이유](#프로젝트-개발이유)
- [프로젝트 개요](#프로젝트-개요)
- [해결한 문제](#해결한-문제)
- [실행 방법](#실행-방법)
- [추가 개발 계획](#추가-개발-계획)
- [문의](#문의)

---
## 팀 소개

### 팀 이름: **어벤져스**

| 이름          | 역할           | GitHub Profile                                          |
|--------------|----------------|----------------------------------------------------------|
| 윤은빈        | 대표 / 프론트 | [@eunbin](https://github.com/eunbin0116/eunbin)            |
| 최선호        | 모델 학습   | [@CSH0805](https://github.com/CSH0805)                       |
| 박수찬        | 데이터 수집     | [@vsssksvss](https://github.com/vsssksvss/vsssksvss)     |
| 윤상림        | 데이터 수집  | [@younsanglim](https://github.com/younsanglim)              |

---
## 프로젝트 개발 이유

- **폭설로 인해 교통 마비, 제설차 이동이 어려운 곳의 미끄러움으로 인한 피해 등등 때문에 생기는 사고를 최소화하고자 함.**
- **이동의 제약이 없는 드론을 사용해서 제설차가 가기 어려운 곳도 제설작업을 수월하게 할 수 있도록 하는 것.**

## 프로젝트 개요

### 프로젝트 이름: **Snow-Detection-System**

### 주요 기능:
- **기능 1**: 드론 카메라 화면으로 눈을 인식. > 웹캠을 통해 눈 인식
- **기능 2**: 인식할 시 드론 기기에 알림 전송. > 눈이라고 인식할 시 폰 이메일로 전송
- **기능 3**: 알림을 받은 드론은 제설 작업 시작. > 눈이 감지 되면 제설 시작

### 기술 스택:
- **백엔드**: Python, teachable machine
- **데이터 셋**: kaggle

---
### 해결한 문제
- **문제 1**: tensorflow를 통해 이미지 분석하려고 했으나 지식이 부족해 실패.
    **해결방법**: teachable machine을 통해 방향성을 새로 잡아 극복.

   
- **문제 2**: 부족한 데이터 수 때문에 AI학습이 원활하게 되지 않음.
    **해결방법**: 직접 4명이서 밖에 나가 필요한 이미지들을 찍어서 사용함. 

---
### 실행 방법
1. 아나콘다 3.12 버전 설치 > 가상환경 설정
2. pip install tensorflow==2.12.1


---

### 시연 영상
[시연영상 보기](https://youtu.be/CcKwUKkrSyI?si=MdUiS20-Vsq3Ww56)

---
### 추가 개발 계획

**1. 개발한 ai를 드론과 연동.
2. 다양한 조건, 비와 눈이나 우박 등의 상황에서 유연하게 대처.
3. 제설 작업 후 보고서 확인 기능**.

## 문의

**프로젝트에 대한 문의 사항은 아래로 연락해주세요:**

- **이메일**: a01022450593@gmail.com

---

### 감사합니다! 👨🏻🧒🏻👧🏻👩🏻‍🦰
