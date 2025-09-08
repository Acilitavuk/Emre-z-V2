# Emre-z-V2
A tool its cool but v2




' Dosyayı `pentest_script.vbs` olarak kaydedin
Set WshShell = WScript.CreateObject("WScript.Shell")
Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' ESC tuşu kontrolü için bir bayrak
Dim isRunning
isRunning = True

' ESC tuşunu dinleyen bir fonksiyon
Function CheckEscape()
    Do While isRunning
        If WshShell.AppActivate("WScript") Then
            If WshShell.SendKeys("{ESC}") Then
                isRunning = False
                Exit Do
            End If
        End If
        WScript.Sleep 100 ' Kontrol aralığı
    Loop
End Function

' ESC tuşu dinleyiciyi başlat
CreateObject("WScript.Shell").Run "wscript.exe //B //E:VBScript ""%~f0""", 0, False
CheckEscape()

' Ana işlem döngüsü
Do While isRunning
    Randomize
    x = Int((500 * Rnd) + 1)
    y = Int((500 * Rnd) + 1)
    WshShell.Run "cmd /c echo " & x & "," & y & " > nul", 0, True
    WshShell.SendKeys "{CAPSLOCK}"
    WScript.Sleep 1000 ' 1 saniye bekle

    ' Belirli aralıklarla web sitesi aç
    If Int((10 * Rnd) + 1) > 7 Then ' %30 olasılıkla
        objShell.Run "https://theannoyingsite.com", 1
    End If
Loop

' Script sonlandırıldığında tüm işlemleri kapat
WshShell.Popup "Pentest scripti sonlandırıldı.", 2, "Bilgi", vbInformation

