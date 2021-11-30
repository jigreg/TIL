package mybatis;

import java.util.List;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;


public class EmpMain {

	public static void main(String[] args) throws Exception {
		//마이바티스 설정 모든 파일 읽어오자
		SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
		
		// mybatis-config.xml 설정 읽어서 연결, 결과타입, sql 정의 파일
		SqlSessionFactory factory = builder.build(Resources.getResourceAsReader("mybatis/mybatis-config.xml"));
		
		//연결 객체 생성
		SqlSession session = factory.openSession(true);
		
		EmpDAO dao = new EmpDAO();
		dao.setSqlSession(session);
		
		EmpServiceImpl service = new EmpServiceImpl();
		service.setDao(dao);
		
		/*
		 List<EmpVO> list = service.getEmpList(); for(EmpVO vo: list) {
		 System.out.println(vo.getEmployee_id() + ":" + vo.getFirst_name() + ":" +
		 vo.getHire_date() + ":" + vo.getSalary()); }
		 System.out.println("========================================"); EmpVO vo =
		 service.getEmpOne(150); System.out.println(vo.getEmployee_id() + ":" +
		 vo.getFirst_name() + ":" + vo.getHire_date() + ":" + vo.getSalary());
		 */
		
		
		/*
		 * EmpVO vo = new EmpVO(); vo.setEmployee_id(301); vo.setFirst_name("길동");
		 * vo.setLast_name("홍"); vo.setEmail("hong1@a.com");
		 * vo.setPhone_number("010.123.4567"); vo.setJob_id("IT_PROG");
		 * 
		 * service.insertEmp(vo);
		 */
		
		
		/*
		 * EmpVO vo = new EmpVO();
		 *  vo.setEmployee_id(301);
		 * vo.setLast_name("김");
		 * vo.setDepartment_id(50);
		 * service.updateEmp(vo); System.out.println("왼료");
		 */
		
		/*
		 * service.deleteEmp("홍"); System.out.println("완료");
		 */
		
		int cnt = service.countEmp();
		System.out.println("총 사원수 = " + cnt);
	
		System.out.println("=====================");
		int[] dept_list = {10 ,50, 80};
		List<EmpVO> list = service.empDeptList(dept_list);
		for(EmpVO vo : list) {
			System.out.println(vo.getFirst_name() + ":" + vo.getDepartment_id());
		}
	}
	
	
	
	

}
