# 1장. 안녕 파이썬!

## 1. 데이터 분석과 파이썬

#### 데이터 분석에서의 파이썬의 쓰임
- 통계분석
- 머신러닝 모델링
- 텍스트 마이닝
- 네트워크 분석
- 지도 시각화
- 주식분석
- 이미지 분석
- 사운드 분석
- 소프트웨어 개발

<br>

## 2. 아나콘다로 파이썬과 JupyterLab 설치

> 설치실습 진행!  
> practices파일 참고!

<br>

## 3. 변수, 함수, 패키지 이해하기

### 1) 변수 이해하기

#### 변수 : 다양한 값을 지닌 하나의 속성
**데이터 분석** : 변수간에 어떤 관계가 있는지 파악하는 작업  
**상수** : 고정값으로 분석대상이 될 수 없다

```python
a=1
b=2

a+b #연산도 가능
```
위와 같은 방식으로 변수를 선언한다.
- 변수명은 알아보기 쉽고 잘 기억되게 의미를 담아야한다.
- 변수명의 시작은 문자로 해야한다.
- 대소문자를 섞어서 변수명을 정하면 오타가 났을 때 파악하기 어려우니 언더바를 이용하자

<br>

### 2) 함수 이해하기
데이터 분석은 결국 함수를 이용해서 변수를 조작하는 일!  
**함수** : 어떠한 기능을 하는 하나의 단위

```python
# 예제에서는 내장함수를 사용했으나 따로 파이썬 함수를 만들어서 사용해도 된다! def!!

sum()  # 리스트의 합을 알려주는 기능을 하는 내장함수
min()  # 리스트에서 가장 작은 값을 알려주는 내장함수
max()  # 리스트에서 가장 큰 값을 알려주는 내장함수
```
<br>

### 3) 함수 꾸러미, 패키지 이해하기
패키지(package) : 어떠한 주제의 함수를 담은 꾸러미  
* 아나콘다에는 주요 패키지가 대부분 들어있다. 
* 패키지를 로드하기 위해저는 import뒤에 패키지 이름을 입력하고 실행한다.
  
  ```python
  # 그래프를 만들 때 많이 사용하는 패키지
  import seaborn as sns
  
  df = sns.load_dataset('titanic')
  df
  
  # 승객 정보 중 성별을 기준으로 그래프를 그려보자
  sns.countplot(data=df, x='sex')
  sns.countplot(data=df, x='class')     # x축은 class
  sns.countplot(data=df, x='class', hue='alive')    # x축은 class, alive별 색 표현
  sns.countplot(data=df, y='class', hue='alive')    # y축이 class, alive별 색 표현

  ```
  위는 타이타닉호 승객정보를 불러오는 함수(load_dataset())와 그래프를 그리는 함수(countplot())를 이용한 예시

<br>

### 4) 모듈 알아보기
**모듈** : 패키지에 함수가 너무나 많기 때문에 비슷한 함수끼리 묶어 몇 가지로 나뉘어놓은 것

```python
# sklearn 패키지의 metrics모듈 로드하기
# sklearn : 머싱러닝 모델 만들 때 사용
# 여러 함수 중 정확도 성능 평가를 위해 accuracy_score()함수를 사용 > metrics 모듈안에 있으니 모듈을 불러와야함
import sklearn.metrics  
sklearn.metrics.accuracy_score()

# 또는
from sklearn import metrics
metrics.accuracy_score()

# 또는
from sklearn.metrics import accuracy_score
accuracy_score()
# import 방법 다 뒤에 약어 붙어도 상관 x
```

> 따로 패키지 설치하고 싶으면 pip 이용하기 
>
[pydataset 설치 후 실습](../practices/day01__variable_def_packages.ipynb)