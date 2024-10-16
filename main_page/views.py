import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from main_page.data_processing import draw_stacked_chart ,save_programming_chart4
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
from wordcloud import WordCloud
import numpy as np
import random

import squarify
from math import pi

from main_page.data_processing import draw_stacked_chart ,save_programming_chart4
"""
도희님 코드
"""
def main_page(request):
    # Pandas로 데이터 처리
    # df = get_programming_data()
    # chart_data = prepare_chart_data(df)
    #seaborn 으로 처리
    chart_path = draw_stacked_chart()
    save_programming_chart4()
    # chart_data를 HTML로 전달
    return render(request, 'main_page/index.html', {'chart_path': chart_path})

def index_test(request):
    # Pandas로 데이터 처리
    # df = get_programming_data()
    # chart_data = prepare_chart_data(df)
    #seaborn 으로 처리
    chart_path = draw_stacked_chart()
    save_programming_chart4()
    # chart_data를 HTML로 전달
    return render(request, 'main_page/index.html', {'chart_path': chart_path})


matplotlib.use('Agg')  # 이거 없으면 서버 꺼짐

# 프로젝트 내부 폰트 경로
# font_path = os.path.join(settings.BASE_DIR, 'main_page', 'static', 'fonts', 'NanumSquareNeo-Variable.ttf')
# font_prop = font_manager.FontProperties(fname=font_path)
# rc('font', family=font_prop.get_name())

font_path = '/Library/Fonts/Arial Unicode.ttf'  # 한글이 안 나와서 폰트 추가함. 근데 맥북 한글 폰트 경로라,, 다른 환경에선 어떡하지
font_prop = font_manager.FontProperties(fname=font_path)
rc('font', family=font_prop.get_name())

def index(request):
    return render(request, 'main_page/index.html')


def main_page(request):
    # Pandas로 데이터 처리
    # df = get_programming_data()
    # chart_data = prepare_chart_data(df)

    #seaborn 으로 처리 
    chart_path = draw_stacked_chart()
    save_programming_chart4()
    # chart_data를 HTML로 전달
    return render(request, 'main_page/index.html', {'chart_path': chart_path})

def index_test(request):
    return render(request, 'main_page/index_test.html')


def generate_colors(num_colors):
    cmap_names = ["Set1", "Paired", "Pastel1", "Accent", "tab10"]
    cmap = plt.get_cmap(random.choice(cmap_names))
    return [cmap(i) for i in range(min(num_colors, cmap.N))]


def save_plot_to_buffer(fig):
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)
    return buffer


def draw_bar_chart(job_titles, new_hires, experienced_hires, colors, x_label, y_label, title):
    # 총 공고 개수 계산
    total_hires = [new + experienced for new, experienced in zip(new_hires, experienced_hires)]

    # 차트 크기 조정
    fig, ax = plt.subplots(figsize=(12, 6))  # 가로 12, 세로 6으로 조정

    # 총 공고 개수 막대 그래프 설정
    x = range(len(job_titles))
    ax.bar(x, total_hires, width=0.4, color=colors, align='center')

    ax.set_xlabel(x_label, fontproperties=font_prop)
    ax.set_ylabel(y_label, fontproperties=font_prop)
    ax.set_title(title, fontproperties=font_prop)

    # x축 tick 조정
    ax.set_xticks(x)
    
    # x축 레이블을 회전하여 표시
    ax.set_xticklabels(job_titles, fontproperties=font_prop, rotation=45, ha='right')
    plt.tight_layout()

    return fig


def draw_double_bar_chart(job_titles, new_hires, experienced_hires, colors, x_label, y_label, title, legend_label_1, legend_label_2):
    x = range(len(job_titles))
    width = 0.3

    fig, ax = plt.subplots(figsize=(12, 6))  # 차트 크기 설정

    # 두 개의 바 차트 그리기
    ax.bar([i - width/2 for i in x], new_hires, width, label=legend_label_1, color=colors[0])
    ax.bar([i + width/2 for i in x], experienced_hires, width, label=legend_label_2, color=colors[1])

    # x축, y축, 제목 설정
    ax.set_xlabel(x_label, fontproperties=font_prop)
    ax.set_ylabel(y_label, fontproperties=font_prop)
    ax.set_title(title, fontproperties=font_prop)
    
    # x축 레이블 설정 및 회전
    ax.set_xticks(x)
    ax.set_xticklabels(job_titles, fontproperties=font_prop, rotation=45, ha='right')  # x축 레이블 회전 및 정렬

    # 범례 표시
    ax.legend()

    # 레이아웃 자동 조정
    plt.tight_layout()

    return fig


# 1번 차트 총 공고 개수
def job_postings_count_chart(request):
    # job_titles = ['백엔드', '프론트엔드', '데이터 엔지니어']
    # new_hires = [10, 5, 8]  # 신입 공고 수
    # experienced_hires = [5, 2, 3]  # 경력 공고 수

    job_titles = ['데이터 엔지니어', '백엔드', '데이터 엔지니어', '데이터 엔지니어', '프론트엔드',
                '백엔드', '프론트엔드', '프론트엔드', '데이터 엔지니어', '백엔드',
                '프론트엔드', '프론트엔드', '데이터 엔지니어', '백엔드', '백엔드',
                '데이터 엔지니어', '데이터 엔지니어', '백엔드', '백엔드', '프론트엔드']

    new_hires = [8, 10, 8, 8, 5, 10, 5, 5, 8, 10, 5, 5, 8, 10, 10, 8, 8, 10, 10, 5]

    experienced_hires = [3, 5, 3, 3, 2, 5, 2, 2, 3, 5, 2, 2, 3, 5, 5, 3, 3, 5, 5, 2]

    # colors = ["#a0b2da", "#dac8a0", "#a0cfda"]
    colors = generate_colors(len(job_titles))
    x_label = "직업"
    y_label = "채용 공고 개수"
    title = "직업별 채용 공고 개수"

    fig = draw_bar_chart(job_titles, new_hires, experienced_hires, colors, x_label, y_label, title)
    buffer = save_plot_to_buffer(fig)

    return HttpResponse(buffer, content_type='image/png')


# 1번 차트 신입/경력 표시
def job_postings_count_by_experience_chart(request):
    job_titles = ['데이터 엔지니어', '백엔드', '데이터 엔지니어', '데이터 엔지니어', '프론트엔드',
                '백엔드', '프론트엔드', '프론트엔드', '데이터 엔지니어', '백엔드',
                '프론트엔드', '프론트엔드', '데이터 엔지니어', '백엔드', '백엔드',
                '데이터 엔지니어', '데이터 엔지니어', '백엔드', '백엔드', '프론트엔드']

    new_hires = [8, 10, 8, 8, 5, 10, 5, 5, 8, 10, 5, 5, 8, 10, 10, 8, 8, 10, 10, 5]

    experienced_hires = [3, 5, 3, 3, 2, 5, 2, 2, 3, 5, 2, 2, 3, 5, 5, 3, 3, 5, 5, 2]

    colors = ["#4192f4", "#92f441"]
    x_label = '직업'
    y_label = '채용 공고 개수'
    title = '직업별 채용 공고 개수'
    legend_label_1 = '신입'
    legend_label_2 = '경력'

    fig = draw_double_bar_chart(job_titles, new_hires, experienced_hires, colors, x_label, y_label, title, legend_label_1, legend_label_2)
    buffer = save_plot_to_buffer(fig)

    return HttpResponse(buffer, content_type='image/png')


def entry_tech_stacks_chart(request):
    # 직업, 기술 스택 개수를 가지는 더미 데이터
    job_title = '데이터 엔지니어'
    entry_tech_stacks = {
        'Python': 11,
        'Django': 40,
        'SQL': 27,
        'JavaScript': 35,
        'React': 22,
        'Node.js': 15,
        'HTML': 29,
        'CSS': 25,
        'Java': 18,
        'C++': 12,
        'Ruby': 14,
        'Go': 10,
        'Swift': 8,
        'Kotlin': 16,
        'PHP': 20,
        'TypeScript': 21,
        'Rust': 7,
        'Scala': 9,
        'R': 13,
        'MATLAB': 6,
        'PowerShell': 4,
        'Shell Scripting': 5,
        'Firebase': 11,
        'MongoDB': 23,
        'PostgreSQL': 17,
        'Redis': 9,
        'GraphQL': 10,
        'Vue.js': 12,
        'Angular': 15,
        'Elixir': 8,
        'ASP.NET': 14,
    }

    total = sum(entry_tech_stacks.values())
    percentages = {key: (value / total) * 100 for key, value in entry_tech_stacks.items()}

    labels = [f"{key}\n{round(percentages[key], 1)}%" for key in entry_tech_stacks.keys()]
    sizes = list(entry_tech_stacks.values())

    # 트리맵 생성
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = plt.cm.Spectral([i / float(len(sizes)) for i in range(len(sizes))])

    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, ax=ax)
    
    plt.title(f'{job_title} 신입', fontsize=20)
    plt.axis('off')  # 축 숨기기

    # 이미지 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')


def experienced_tech_stacks_chart(request):
    # 직업, 기술 스택 개수를 가지는 더미 데이터
    job_title = '데이터 엔지니어'
    experienced_tech_stacks = {
        'Docker': 15,
        'Kubernetes': 35,
        'Hadoop': 28,
        'Spark': 42,
        'Kafka': 19,
        'Airflow': 33,
        'Flink': 25,
        'Redshift': 14,
        'Snowflake': 30,
        'BigQuery': 22,
        'ElasticSearch': 18,
        'Terraform': 12,
        'Ansible': 27,
        'Jenkins': 21,
        'AWS': 45,
        'Azure': 16,
        'GCP': 23,
        'Databricks': 34,
        'Presto': 17,
        'Hive': 26,
        'Cassandra': 13,
        'MongoDB': 31,
        'MySQL': 20,
        'PostgreSQL': 29,
        'Redis': 11,
        'Druid': 9,
        'RabbitMQ': 24,
        'Zookeeper': 8,
        'Vault': 6,
        'Consul': 7
    }

    total = sum(experienced_tech_stacks.values())
    percentages = {key: (value / total) * 100 for key, value in experienced_tech_stacks.items()}

    labels = [f"{key}\n{round(percentages[key], 1)}%" for key in experienced_tech_stacks.keys()]
    sizes = list(experienced_tech_stacks.values())

    # 트리맵 생성
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = plt.cm.Spectral([i / float(len(sizes)) for i in range(len(sizes))])

    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, ax=ax)
    
    plt.title(f'{job_title} 경력', fontsize=20)
    plt.axis('off')  # 축 숨기기

    # 이미지 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')

"""
3번 도표
donut_chart
"""
# def display_entry_tech_stacks(request):
#     # logger.info("donut_chart view called")

#     # 직업, 기술 스택 개수를 가지는 더미 데이터
#     job_title = '데이터 엔지니어'
#     entry_tech_stacks = {
#     'Python': 11,
#     'Django': 40,
#     'SQL': 27,
#     'JavaScript': 35,
#     'React': 22,
#     'Node.js': 15,
#     'HTML': 29,
#     'CSS': 25,
#     'Java': 18,
#     'C++': 12,
#     'Ruby': 14,
#     'Go': 10,
#     'Swift': 8,
#     'Kotlin': 16,
#     'PHP': 20,
#     'TypeScript': 21,
#     'Rust': 7,
#     'Scala': 9,
#     'R': 13,
#     'MATLAB': 6,
#     'PowerShell': 4,
#     'Shell Scripting': 5,
#     'Firebase': 11,
#     'MongoDB': 23,
#     'PostgreSQL': 17,
#     'Redis': 9,
#     'GraphQL': 10,
#     'Vue.js': 12,
#     'Angular': 15,
#     'Elixir': 8,
#     'ASP.NET': 14,
# }

#     total = sum(entry_tech_stacks.values())
#     percentages = [(count / total) * 100 for count in entry_tech_stacks.values()]

#     labels = list(entry_tech_stacks.keys())
#     sizes = percentages
#     colors = generate_colors(len(entry_tech_stacks))

#     # 도넛 차트 생성
#     fig, ax = plt.subplots()
#     wedges, texts = ax.pie(sizes, labels=labels, startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'))

#     # 도넛 모양 만들기
#     centre_circle = plt.Circle((0, 0), 0.70, fc='white')  
#     fig.gca().add_artist(centre_circle)

#     ax.axis('equal')  # 비율 유지
#     plt.title('기술 스택 비율')

#     # 가운데에 직군 표시
#     plt.text(0, 0, job_title, ha='center', va='center', fontsize=16, fontweight='bold')

#     # 퍼센트 텍스트 위치 조정
#     for i, wedge in enumerate(wedges):
#         angle = (wedge.theta1 + wedge.theta2) / 2
#         x = np.cos(np.radians(angle)) * 0.85
#         y = np.sin(np.radians(angle)) * 0.85
#         percentage = round(percentages[i], 1)
#         plt.text(x, y, f'{percentage}%', ha='center', va='center', fontsize=10, fontweight='bold')


#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close(fig)

#     return HttpResponse(buffer, content_type='image/png')


# def donut_chart(request):
#     # logger.info("donut_chart view called")

#     # 직업, 기술 스택 개수를 가지는 더미 데이터
#     job_title = '데이터 엔지니어'
#     experienced_tech_stack = {
#     'Python': 11,
#     'Django': 40,
#     'SQL': 27,
#     'JavaScript': 35,
#     'React': 22,
#     'Node.js': 15,
#     'HTML': 29,
#     'CSS': 25,
#     'Java': 18,
#     'C++': 12,
#     'Ruby': 14,
#     'Go': 10,
#     'Swift': 8,
#     'Kotlin': 16,
#     'PHP': 20,
#     'TypeScript': 21,
#     'Rust': 7,
#     'Scala': 9,
#     'R': 13,
#     'MATLAB': 6,
#     'PowerShell': 4,
#     'Shell Scripting': 5,
#     'Firebase': 11,
#     'MongoDB': 23,
#     'PostgreSQL': 17,
#     'Redis': 9,
#     'GraphQL': 10,
#     'Vue.js': 12,
#     'Angular': 15,
#     'Elixir': 8,
#     'ASP.NET': 14,
# }

#     total = sum(experienced_tech_stack.values())
#     percentages = [(count / total) * 100 for count in experienced_tech_stack.values()]

#     labels = list(experienced_tech_stack.keys())
#     sizes = percentages
#     colors = generate_colors(len(experienced_tech_stack))

#     # 도넛 차트 생성
#     fig, ax = plt.subplots()
#     wedges, texts = ax.pie(sizes, labels=labels, startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'))

#     # 도넛 모양 만들기
#     centre_circle = plt.Circle((0, 0), 0.70, fc='white')  
#     fig.gca().add_artist(centre_circle)

#     ax.axis('equal')  # 비율 유지
#     plt.title('기술 스택 비율')

#     # 가운데에 직군 표시
#     plt.text(0, 0, job_title, ha='center', va='center', fontsize=16, fontweight='bold')

#     # 퍼센트 텍스트 위치 조정
#     for i, wedge in enumerate(wedges):
#         angle = (wedge.theta1 + wedge.theta2) / 2
#         x = np.cos(np.radians(angle)) * 0.85
#         y = np.sin(np.radians(angle)) * 0.85
#         percentage = round(percentages[i], 1)
#         plt.text(x, y, f'{percentage}%', ha='center', va='center', fontsize=10, fontweight='bold')


#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close(fig)

#     return HttpResponse(buffer, content_type='image/png')


"""
3번 도표 layered_donut_chart
"""
# def layered_donut_chart(request):
#     # 직군과 해당 기술 스택 및 개수 정의
#     job_label = 'Data Engineer'  # 중심에 표시할 직군 이름
#     sizes_new = [11, 5, 33]  # 신입 레이어 데이터
#     sizes_experienced = [15, 48, 21]  # 경력 레이어 데이터
#     labels = ['Python', 'SQL', 'Django']  # 공통 기술 스택
#     colors = ['#ff9999', '#66b3ff', '#99ff99']  # 도넛 색상

#     fig, ax = plt.subplots()

#     # 경력 레이어 (바깥 도넛)
#     total_experienced = sum(sizes_experienced)
#     percentages_experienced = [(count / total_experienced) * 100 for count in sizes_experienced]

#     wedges1, texts1 = ax.pie(
#         percentages_experienced,
#         radius=1,  # 바깥 도넛
#         startangle=90,
#         labels=labels,
#         colors=colors,
#         wedgeprops=dict(width=0.3, edgecolor='w')  # 두께와 경계선
#     )

#     # 신입 레이어 (내부 도넛)
#     total_new = sum(sizes_new)
#     percentages_new = [(count / total_new) * 100 for count in sizes_new]

#     wedges2, texts2 = ax.pie(
#         percentages_new,
#         radius=0.7,  # 내부 도넛
#         startangle=90,
#         colors=colors,
#         wedgeprops=dict(width=0.3, edgecolor='w')  # 두께와 경계선
#     )

#     # 가운데 흰 원 추가 (직군 이름을 쓸 자리)
#     centre_circle = plt.Circle((0, 0), 0.4, fc='white')  # 흰 원 크기를 조절하여 비율 조정
#     fig.gca().add_artist(centre_circle)

#     # 가운데에 직군 이름 표시하는 건데 도표랑 겹쳐서 뺌
#     # plt.text(0, 0, job_label, ha='center', va='center', fontsize=18, fontweight='bold')

#     ax.axis('equal')  # 비율 유지
#     plt.title(f'기술 스택 비율 - {job_label}', fontsize=14)

#     # 퍼센트 텍스트 위치 조정 (경력 레이어)
#     for i, wedge in enumerate(wedges1):
#         angle = (wedge.theta1 + wedge.theta2) / 2  # 각도 계산
#         x = np.cos(np.radians(angle)) * 0.85  # 위치 조정
#         y = np.sin(np.radians(angle)) * 0.85
#         percentage = round(percentages_experienced[i], 1)  # 정수로 변환
#         plt.text(x, y, f'{percentage}%', ha='center', va='center', color='black', fontsize=14, fontweight='bold')

#     # 퍼센트 텍스트 위치 조정 (신입 레이어)
#     for i, wedge in enumerate(wedges2):
#         angle = (wedge.theta1 + wedge.theta2) / 2  # 각도 계산
#         x = np.cos(np.radians(angle)) * 0.58  # 위치 조정
#         y = np.sin(np.radians(angle)) * 0.5
#         percentage = round(percentages_new[i], 1)  # 정수로 변환
#         plt.text(x, y, f'{percentage}%', ha='center', va='center', color='black', fontsize=14, fontweight='bold')

#     plt.text(1.5, 0, '내부: 신입', ha='center', va='center', fontsize=14, fontweight='bold')
#     plt.text(1.5, -0.15, '외부: 경력', ha='center', va='center', fontsize=14, fontweight='bold')

#     # 이미지 저장
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     plt.close(fig)

#     return HttpResponse(buffer, content_type='image/png')


"""
3번 도표
워드 클라우드
"""
# def word_cloud(request):
#     # 직군 정의
#     job_label = '데이터 엔지니어'
#     tech_stacks = {
#         'Python': 25,
#         'Django': 30,
#         'SQL': 20,
#         'Java': 1,
#         'docker': 5
#     }
#     wordcloud = WordCloud(
#         font_path='/Users/huh_zz/Downloads/NanumSquareNeo/NanumSquareNeo-Variable.ttf',
#         background_color='white',
#         height=800,  # 워드 클라우드 높이 조정
#         width=800    # 워드 클라우드 너비 조정
#     )
    
#     img = wordcloud.generate_from_frequencies(tech_stacks)

#     # 플롯 설정
#     plt.figure(figsize=(10, 5))  # 플롯 크기 조정 (인치 단위)
#     plt.imshow(img, interpolation='bilinear')

#     # 제목 추가
#     plt.title(f'{job_label}', fontsize=14, fontweight='bold', pad=20)
#     plt.axis('off')  # 축 제거

#     plt.subplots_adjust(bottom=0.15)

#     # 이미지 저장
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.5)  # 여백 조정
#     buffer.seek(0)
#     plt.close()

#     return HttpResponse(buffer, content_type='image/png')


"""
3번 도표
word_cloud
신입
"""
def word_cloud_new(request):
    job_label = '데이터 엔지니어'
    tech_stacks_new = {
        'Python': 25,
        'Django': 30,
        'SQL': 20,
        'Java': 1,
        'Docker': 5
    }
    
    # 신입 워드 클라우드 생성
    wordcloud = WordCloud(
        font_path='/Users/huh_zz/Downloads/NanumSquareNeo/NanumSquareNeo-Variable.ttf',
        background_color='white',
        height=800,
        width=800
    ).generate_from_frequencies(tech_stacks_new)

    # 플롯 설정
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'{job_label} (신입)', fontsize=14, fontweight='bold', pad=20)
    plt.axis('off')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.5)
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')


"""
3번 도표
word_cloud
경력
"""
def word_cloud_experienced(request):
    job_label = '데이터 엔지니어'
    tech_stacks_experienced = {
        'Python': 30,
        'Django': 35,
        'SQL': 25,
        'Java': 10,
        'Docker': 15
    }
    
    # 경력 워드 클라우드 생성
    wordcloud = WordCloud(
        font_path='/Users/huh_zz/Downloads/NanumSquareNeo/NanumSquareNeo-Variable.ttf',
        background_color='white',
        height=800,
        width=800
    ).generate_from_frequencies(tech_stacks_experienced)

    # 플롯 설정
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'{job_label} (경력)', fontsize=14, fontweight='bold', pad=20)
    plt.axis('off')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.5)
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')
