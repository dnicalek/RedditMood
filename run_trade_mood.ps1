$redditScriptPath = "D:\PyCharmProjects\RedditMood\reddit_data_downloader.py"
$mainScriptPath = "D:\PyCharmProjects\RedditMood\main_processor.py"

$redditScriptTime = "04:00"
$mainScriptTime = "04:10"

while ($true) {
    $currentTime = Get-Date -Format "HH:mm"

    if ($currentTime -eq $redditScriptTime) {
        Start-Process "python.exe" -ArgumentList "$redditScriptPath"
        break
    }

    if ($currentTime -eq $mainScriptTime) {
        Start-Process "python.exe" -ArgumentList "$mainScriptPath"
        break
    }

    Start-Sleep -Seconds 60
}
