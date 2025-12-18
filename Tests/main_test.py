import pytest
from main import solution, solve, disc_counter
# test 1
@pytest.mark.parametrize(
    'x,y,z,expected',
    ((1, 8, 15, (-3.0, -5.0)),
     (1, -13, 12, (12.0, 1.0)),
     (-4, 28, -49, (3.5)),
     (1, 1, 1, ('корней нет')))
)
def test_solution(x, y, z, expected):
    assert solution(x, y, z) == expected
# test 2
@pytest.mark.parametrize(
    'boys,girls,expected',
    [
        (['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        "Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha"),

        (['Peter', 'Alex', 'John', 'Arthur'],
        ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
        "Кто-то может остаться без пары!"),

        (['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
        ['Kate', 'Liza', 'Kira', 'Emma'],
        "Кто-то может остаться без пары!")
     ]
)
def test_(boys, girls, expected):
    assert solve(boys, girls) == expected

# test 3
@pytest.mark.parametrize(
    'models,available,manufacturers,expected',
    [
        (['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
   '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
   '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
   '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500'],
        [1, 1, 1, 1, 0, 1, 1, 0],
        ['Intel', 'Samsung', 'WD'],
        (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2))
     ]
)
def test_disc_counter(models, available, manufacturers, expected):
    assert disc_counter(models, available, manufacturers) == expected
