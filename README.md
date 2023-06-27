# football-data-pipeline
### About this project

### Used Methods
1. Google Cloud Platform
   - Google Cloud Storage for datalake
   - Google Cloud SQL for database to store repeatable key parameters for API
   - Google Cloud Engines (Ubuntu Base) for API requests, Prometheus&Grafana
2. Airflow
3. cron

### Airflow DAG Structure
1. TEST structure for the local environment(M2 PRO MAC)

### Status
#### 23.06.24
- made modules for API requests (URI making, JSON loading)
- TEST at local environments (for Players/Players Data)
- 

### Tree - 23.06.27
```
.
├── README.md
├── dags
│   └── extract
│       └── neivekim76
│           ├── __pycache__
│           │   └── extract_players.cpython-37.pyc
│           └── extract_players.py
├── datas
│   └── JSON
│       └── season_22
│           └── players
│               ├── players_103_2144_2022_1.json
│               ├── players_103_2144_2022_2.json
│               ├── players_103_2144_2022_3.json
│               .  
│               .  
│               .  
│               .
│               ├── players_98_316_2022_3.json
│               ├── players_98_316_2022_4.json
│               └── players_98_316_2022_5.json
├── lib
│   ├── __pycache__
│   │   └── football_lib.cpython-37.pyc
│   └── football_lib.py
├── sh
└── src
    ├── API_requests
    │   └── neivekim76
    │       └── make_JSON_players.py
    └── uri
        └── neivekim76
            └── make_uri_players.py
```
