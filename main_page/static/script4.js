// const programmingData = [{
//         "lang": "Java",
//         "jobs": [
//             { "job": "백엔드 개발자", "percentage": 30 },
//             { "job": "자바 개발자", "percentage": 30 },
//             { "job": "웹 개발자", "percentage": 40 }
//         ]
//     },
//     {
//         "lang": "Python",
//         "jobs": [
//             { "job": "백엔드 개발자", "percentage": 25 },
//             { "job": "데이터 엔지니어", "percentage": 35 },
//             { "job": "프론트엔드 개발자", "percentage": 40 }
//         ]
//     },
//     {
//         "lang": "JavaScript",
//         "jobs": [
//             { "job": "프론트엔드 개발자", "percentage": 50 },
//             { "job": "풀스택 개발자", "percentage": 30 },
//             { "job": "웹 퍼블리셔", "percentage": 20 }
//         ]
//     },
//     {
//         "lang": "C",
//         "jobs": [
//             { "job": "임베디드 개발자", "percentage": 10 },
//             { "job": "IOT 개발자", "percentage": 50 },
//             { "job": "코어뱅킹 개발자", "percentage": 40 }
//         ]
//     }
// ];

let myChart4; // 차트 인스턴스

// 프로그래밍 언어 기준 해당 언어를 많이 쓰는 직업 Top 3 차트 그리기
function drawProgrammingChart(programmingData) {
    const ctx = document.getElementById('myChart4').getContext('2d');

    // 기존 차트가 있다면 제거
    if (myChart4) {
        myChart4.destroy();
    }

    // 데이터 가공
    const labels = Object.keys(programmingData);
    const datasets = [];

    // 각 프로그래밍 언어에 대해 직업 데이터를 추가
    const jobs = ["백엔드 개발자", "자바 개발자", "웹 개발자", "데이터 엔지니어", "프론트엔드 개발자", "풀스택 개발자", "웹 퍼블리셔", "임베디드 개발자", "IOT 개발자", "코어뱅킹 개발자"];
    const jobColors = [
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        'rgba(153, 102, 255, 0.6)',
        'rgba(255, 159, 64, 0.6)',
        'rgba(201, 203, 207, 0.6)',
        'rgba(100, 100, 255, 0.6)',
        'rgba(100, 255, 100, 0.6)',
        'rgba(255, 100, 100, 0.6)'
    ];

    jobs.forEach((job, index) => {
        datasets[index] = {
            label: job,
            data: [],
            backgroundColor: jobColors[index],
            borderColor: jobColors[index].replace('0.6', '1'), // 경계 색상
            borderWidth: 1,
            barPercentage: 0.8 // 막대기 너비
        };
    });

    labels.forEach((language, languageIndex) => {
        programmingData[language].forEach((jobData, jobIndex) => {
            const jobIndexInArray = jobs.indexOf(jobData.job);
            datasets[jobIndexInArray].data[languageIndex] = jobData.percentage;
        });
    });

    const config = {
        type: 'bar',
        data: {
            labels: labels,
            datasets: datasets,
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: '비율 (%)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: '프로그래밍 언어'
                    },
                    stacked: false, // 막대기 스택을 비활성화
                    grid: {
                        display: false // 그리드 제거
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: '프로그래밍 언어 기준 해당 언어를 많이 쓰는 직업 Top 3'
                }
            },
            barPercentage: 0.6, // 각 언어의 막대기를 가깝게 배치
            categoryPercentage: 0.6 // 카테고리 내 막대기 배치
        }
    };
    myChart4 = new Chart(ctx, config);
}

function draw_chart1(programmingData) {
    const opacity = 0.3; // 70% 불투명도
    const hue = Math.random() * 360; // 색상 값 (Hue)
    const barData = [];
    programmingData.forEach(langData => {
        langData.jobs.forEach(job => {
            barData.push({
                x: [langData.lang], // x축은 언어
                y: [job.percentage], // y축은 직업 비율
                name: job.job, // 직업 이름
                type: 'bar', // 막대 차트
                // 각 직업에 대해 다른 색상 설정
                marker: { color: `rgba(${hue}), 70%, 50%, ${opacity})` },
                text: job.percentage + '%', // 비율 표시
                textposition: 'auto' // 비율 텍스트 위치
            });
        });
    });

    const barLayout = {
        title: 'Programming Languages Job Distribution (Job-wise)',
        xaxis: { title: 'Programming Language' },
        yaxis: { title: 'Percentage' },
        barmode: 'stack', // 막대를 쌓아 올리는 형태로 설정
        showlegend: true
    };

    // 막대 차트 생성
    Plotly.newPlot('bar-chart', barData, barLayout);


}