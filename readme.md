
## git link with local 
```
cd ~/
ls -la
mkdir .ssh
cd .ssh
ssh-keygen.exe
```

-- if above command not found then run below to connect to GitHub ashokbalusu account SSH key generation
```
ssh-keygen -t rsa -C "ashokbalusu@hotmail.com"

ls -la
cat id_rsa.pub
```

-- got to GitHub - Settings - SSH and GPG keys - click 'new SSH' - paste above id_rsa.pub value in 'Key' and give a name to 'Title'

-- create a .gitignore and add below lines
```
.gitignore
.venv/
venv/
```


-- below are git setup basic commands
```
git config --list
$ git config --global user.name "Your Name"
git config --global user.name "Your Name"
git config --global user.email "your.name@youraddress.com"
```

-- below are optional to set
```
git config --global push.default matching
git config --global alias.co checkout
```

-- initialize Git
```
git init
```

-- on GitHub.com, create a new repository named 'apps'
-- push an existing repository from the command line
```
git remote add origin git@github.com:ashokbalusu/apps.git
git branch -M main
git push -u origin main
```
