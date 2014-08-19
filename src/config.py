top_dir = ''
target  = ''
log_dir = ''
jobs    = 0
env_file = ''

def dump():
    print '=============== Dump config ================='
    print 'top_dir=', top_dir
    print 'target=' , target
    print 'log_dir=' , log_dir
    print 'jobs=' , jobs
    print 'env_file=' , env_file
    print '============================================='

def validate():
    # TODO
    # 1. validate top_dir
    # 2. validate log_dir and make dir
    # 3. validate jobs
    # 4. validate env_file
    return True
