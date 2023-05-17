from src.models import db, FiliaUser, PhotoPost

def test_profile_page(test_client):
    resp = test_client.get('/profile_page/0')
    assert resp.status_code == 200
    assert b'Profile Page' in resp.data

    other_prof = FiliaUser(firstname='Laya', lastname='Srinivasan', email='laya@uncc.edu', phone='1234567891', gender='female', major='afs_ba', grad_date='fall2023', bio='abc', profile_path='/static/profile-pics/laya.jpeg', username='layaS', password='serfvhnk234vhb2')
    user_id = other_prof.user_id
    resp = test_client.get('/profile_page/user_id')
    assert resp.status_code == 200
    assert b'Profile Page' in resp.data