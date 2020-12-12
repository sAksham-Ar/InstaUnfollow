$value=Test-Path ("$pwd"+"\chromedriver.exe")
pip3 install selenium
if($value -notmatch 'True')
{

Write-Output "Downloading chrome driver"
$ver=(Get-Item (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe').'(Default)').VersionInfo.ProductVersion
$client = new-object System.Net.WebClient
$URI="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"+$ver[0]+$ver[1]
$HTML=Invoke-WebRequest -Uri $URI
$driver=$HTML.Content
$client.DownloadFile("https://chromedriver.storage.googleapis.com/"+$driver+"/chromedriver_win32.zip","$PWD"+'\chromedriver_win32.zip')
Expand-Archive -LiteralPath ("$PWD"+"\chromedriver_win32.zip") -DestinationPath "$pwd"
Remove-Item -Path ("$PWD"+"\chromedriver_win32.zip")
}
$key=Test-Path ("$pwd"+'\key.txt')
if($key -notmatch 'True')
{
$name = Read-Host 'What is your username?'
$pass = Read-Host 'What is your password?' -AsSecureString
$path="$pwd"+"\key.txt"
$name | Out-File -FilePath $path
[Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [Runtime.InteropServices.Marshal]::SecureStringToBSTR($pass)) | Out-File -FilePath $path -Append
}
$path="$pwd"+"\key.txt"
$file_data = Get-Content -Path $path 
$username=$file_data[0]
$password=$file_data[1]
python3 unfollow.py $username $password