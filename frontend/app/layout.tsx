export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ar" dir="rtl">
      <body style={{margin:0,fontFamily:'sans-serif',background:'#fff',color:'#111'}}>
        <header style={{padding:'12px 16px',borderBottom:'1px solid #eee',display:'flex',gap:16,alignItems:'center'}}>
          <div style={{width:120,height:32,background:'#f1f1f1',display:'flex',alignItems:'center',justifyContent:'center'}}>LOGO</div>
          <nav style={{display:'flex',gap:12}}>
            <a href="/">اللوحة</a>
            <a href="/inventory">المخزون</a>
          </nav>
        </header>
        <main style={{padding:'16px'}}>{children}</main>
      </body>
    </html>
  )
}