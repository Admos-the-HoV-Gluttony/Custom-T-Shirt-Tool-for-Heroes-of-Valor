Option Explicit

Dim WshShell, objFSO, downloadUrl, zipFile, extractPath, result, folder

Set WshShell = WScript.CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

downloadUrl = "https://github.com/Admos-the-HoV-Gluttony/Custom-T-Shirt-Tool-for-Heroes-of-Valor/archive/refs/heads/main.zip"
zipFile = WshShell.ExpandEnvironmentStrings("%TEMP%\main.zip")
extractPath = ".."

result = MsgBox("Update the Custom T-Shirt Tool for Heroes of Valor?" & vbCrLf _
              & "The current version will be replaced.", vbYesNo + vbQuestion, "Update Confirmation")

If result = vbNo Then
    WshShell.Popup "Update cancelled..", 5, "Update Cancelled", vbInformation
    WScript.Quit
End If

WshShell.Run "powershell -Command ""(New-Object Net.WebClient).DownloadFile('" & downloadUrl & "', '" & zipFile & "')""", 0, True

If Not objFSO.FileExists(zipFile) Then
    WshShell.Popup "Failed to download the ZIP file.", 5, "Error", vbCritical
    WScript.Quit
End If

WshShell.Run "powershell -Command ""Expand-Archive -Path '" & zipFile & "' -DestinationPath '" & extractPath & "' -Force""", 0, True

If Not objFSO.FolderExists(extractPath) Then
    WshShell.Popup "Extraction path does not exist: " & extractPath, 5, "Error", vbCritical
    WScript.Quit
End If

On Error Resume Next
Set folder = objFSO.GetFolder(extractPath)
If Err.Number <> 0 Then
    WshShell.Popup "Failed to get folder object for: " & extractPath & vbCrLf & Err.Description, 5, "Error", vbCritical
    WScript.Quit
End If
On Error GoTo 0

If folder.Files.Count > 0 Or folder.SubFolders.Count > 0 Then
    WshShell.Popup "Extraction complete.", 5, "Success", vbInformation
Else
    WshShell.Popup "Failed to extract the ZIP file. No files or subfolders found in: " & extractPath, 5, "Error", vbCritical
    WScript.Quit
End If

objFSO.DeleteFile zipFile

WshShell.Popup "Update completed successfully.", 5, "Update Complete", vbInformation