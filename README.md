# Emre-z-V2
A tool its cool but v2






Set WshShell = WScript.CreateObject("WScript.Shell")
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")


Dim isRunning
isRunning = True

Function CheckEscape()
    Do While isRunning
        If WshShell.AppActivate("WScript") Then
            If WshShell.SendKeys("{ESC}") Then
                isRunning = False
                Exit Do
            End If
        End If
    
    Loop
End Function


CreateObject("WScript.Shell").Run "wscript.exe //B //E:VBScript ""%~f0""", 0, False

CheckEscape()
Do While isRunning
    Randomize
    x = Int((500 * Rnd) + 1)
    y = Int((500 * Rnd) + 1)
    WshShell.Run "cmd /c echo " & x & "," & y & " > nul", 0, True
    WshShell.SendKeys "{CAPSLOCK}"
    WScript.Sleep 1000 ' 1 saniye bekle

    
    If Int((10 * Rnd) + 1) > 7 Then ' %30 olasılıkla
        objShell.Run "https://theannoyingsite.com", 1
    End If
Loop


WshShell.Popup "Pentest scripti sonlandırıldı.", 2, "Bilgi", vbInformation

