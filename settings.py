from os import environ

SESSION_CONFIGS = [
    dict(
       name='pre_survey',
       display_name="Pre Survey",
       num_demo_participants=1,
       app_sequence=['pre_survey']
    ),
    dict(
        name='skill_task_part1',
        display_name="Skill tasks part 1 + treatment",
        num_demo_participants=4,
        app_sequence=['skill_task_part1','Investment_game_part1','treatment','Investment_game_part2','skill_task_part2','Summary']
    ),
    # dict(
    #     name='Investment_game_part1',
    #     display_name="Investment_game_part1",
    #     num_demo_participants=1,
    #     app_sequence=['Investment_game_part1']
    # ),
    # dict(
    #     name='Investment_game_part2',
    #     display_name="Investment_game_part2",
    #     num_demo_participants=1,
    #     app_sequence=['Investment_game_part2']
    # ),
    # dict(
    #     name='skill_task_part2',
    #     display_name="Skill tasks part 2",
    #     num_demo_participants=1,
    #     app_sequence=['skill_task_part2']
    # ),
    dict(
       name='demographics_survey',
       display_name="Demographics Survey",
       num_demo_participants=3,
       app_sequence=['demographics_survey']
    ),
    dict(
       name='skill_task',
       display_name="skill_task",
       num_demo_participants=1,
       app_sequence=['skill_task']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'ym%(vjrw%qih!nya*@&)_^qleu9rgir(j+_bkw3y9bedr$jpeq'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
